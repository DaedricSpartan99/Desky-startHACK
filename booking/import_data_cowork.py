import traceback
import csv
from django.db.utils import IntegrityError
from booking.models import Coworking

def import_script(path):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Attempt to get the city by href, or create a new one if it doesn't exist
                cow, created = Coworking.objects.get_or_create(
                    title= row['title'],
                    href=row['href'], 
                    description=row['description'],
                    starting_price=row['starting_price'],
                    image_url=row['image_link'] 
                )
                
 
            except IntegrityError as e:
                print(f"An error occurred: {e}")
                print(traceback.format_exc())
            except City.DoesNotExist:
                print(f"City does not exist for row: {row}")
                print(traceback.format_exc())
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print(traceback.format_exc())

import_script('external/coworking_milan.csv')
import_script('external/coworking_rome.csv')

