import requests
from datetime import datetime, timedelta
import pandas as pd

def fetch_and_save_climate_data():
    # Calculate current date and end date
    current_date = datetime.now().strftime('%Y-%m-%d')
    end_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    # Construct URL with current and end dates
    url = (
        "https://services.cehub.syngenta-ais.com/api/Forecast/ShortRangeForecastDaily"
        "?format=json&supplier=Meteoblue&startDate={}&endDate={}"
        "&measureLabel=TempAir_DailyAvg%20(C);TempAir_DailyMax%20(C);TempAir_DailyMin%20(C);"
        "Precip_DailySum%20(mm);WindDirection_DailyAvg%20(Deg);WindSpeed_DailyAvg%20(m/s);"
        "HumidityRel_DailyAvg%20(pct);WindDirection_DailyAvg;Soilmoisture_0to10cm_DailyAvg%20(vol%25);"
        "WindGust_DailyMax%20(m/s);Referenceevapotranspiration_DailySum%20(mm);"
        "TempSurface_DailyAvg%20(C);Soiltemperature_0to10cm_DailyAvg%20(C)"
        "&latitude=47&longitude=7"
    ).format(current_date, end_date)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'ApiKey': 'your_api_key_here'  # Replace with the actual API key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data_dict = response.json()

        # Convert to DataFrame
        df = pd.DataFrame(data_dict)

        # You may want to rename columns based on your needs here
        # df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)

        # Save to CSV
        csv_file_path = 'climate_data.csv'
        df.to_csv(csv_file_path, index=False)

        print(f"Data successfully fetched and saved to {csv_file_path}")
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

if __name__ == "__main__":
    fetch_and_save_climate_data()
