import traceback
import csv
from django.db.utils import IntegrityError
from booking.models import Workplace, City, User  

with open('/Users/peter/Downloads/Desky/external/city_links.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Attempt to get the city by href, or create a new one if it doesn't exist
            city, created = City.objects.get_or_create(
                href=row['href'], 
                name= row['city']
            )
            
            # Proceed to create the workplace
            """
            workplace = Workplace.objects.create(
                name=row['title'],
                city=city,
                image=row['image_url'],  # Make sure the CSV header matches the field name
                address=row['address'],
                country=row['country'],
                # ... include other fields as necessary
            )
            """

        except IntegrityError as e:
            print(f"An error occurred: {e}")
            print(traceback.format_exc())
        except City.DoesNotExist:
            print(f"City does not exist for row: {row}")
            print(traceback.format_exc())
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(traceback.format_exc())
