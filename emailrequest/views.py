import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings  # To use variables defined in Django's settings.py

from django.http import JsonResponse
#from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
#from rest_framework.parsers import JSONParser

from  datetime import datetime, timedelta
import json
import requests
import pandas as pd
from django.views.decorators.csrf import csrf_exempt


#@require_http_methods(["POST"])  # Assuming you want the action to be triggered by a POST request
@csrf_exempt
@api_view(['POST'])
def trigger_email_view(request):

    #data = JSONParser().parse(request)

    # Logic to trigger the sending of the email, including generating the CSV file path
    if 'recipient' not in request.data:
        return JsonResponse({"message": "Missing recipient."}, status=400)

    recipient = request.data['recipient']
    latitude = request.data['latitude']
    longitude = request.data['longitude']

    print("Recipient: ", recipient)
    print("Latitude: ", latitude)
    print("Longitude: ", longitude)

    df = fetch_data(int(latitude), int(longitude))

    trigger_email_sending(df, recipient)  # Call the function you defined earlier in views.py
    return JsonResponse({"message": "Email has been sent."})

def send_email(df, subject, body, to_email):
    from_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD  # Securely sourced from settings

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body to email
    msg.attach(MIMEText(body, 'plain'))

    filename = 'climate_data.csv'  # Extract filename from path

    # Attach CSV file
    try:
        
        df.to_csv(filename, index=False)

        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")
            msg.attach(part)

    except IOError:
        print(f"Could not open attachment file {filename}.")
        return


    # Send the email
    server=None

    try:
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        #server.ehlo()
        server.starttls()
        #server.ehlo()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    finally:
        if server is not None:
            server.quit()

def fetch_data(latitude, longitude):
    # Calculate current date and end date
    current_date = datetime.now().strftime('%Y-%m-%d')
    end_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    # Construct URL with current and end dates
    url = f"https://services.cehub.syngenta-ais.com/api/Forecast/ShortRangeForecastDaily?format=json&supplier=Meteoblue&startDate={current_date}&endDate={end_date}&measureLabel=TempAir_DailyAvg%20(C);TempAir_DailyMax%20(C);TempAir_DailyMin%20(C);Precip_DailySum%20(mm);WindDirection_DailyAvg%20(Deg);WindSpeed_DailyAvg%20(m/s);HumidityRel_DailyAvg%20(pct);WindDirection_DailyAvg;Soilmoisture_0to10cm_DailyAvg%20(vol%25);WindGust_DailyMax%20(m/s);Referenceevapotranspiration_DailySum%20(mm);TempSurface_DailyAvg%20(C);Soiltemperature_0to10cm_DailyAvg%20(C)&latitude={latitude}&longitude={longitude}"

    payload = {}
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'ApiKey': 'b7b50ace-5063-4897-bfe5-436ec04b904b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data_dict = json.loads(data)

    # Convert to DataFrame
    df = pd.DataFrame(data_dict)

    # Rename columns
    df.columns = ['latitude', 'longitude', 'date', 'measureLabel', 'dailyValue']

    return df

# Assuming this function is called from somewhere within your Django app:
def trigger_email_sending(df, recipient_email):

    email_subject = 'Desky Farm - CSV Data'
    email_body = 'Please find attached the CSV data containing several climate forecasts of the next 2 weeks, we are thrilled to see what you can depict from them.'

    send_email(df, email_subject, email_body, recipient_email)
