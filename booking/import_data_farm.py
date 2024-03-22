import traceback
import csv
from django.db.utils import IntegrityError
from booking.models import Farm, City

with open('./external/wwoofing.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            city, city_created = City.objects.get_or_create(name=row['city'])

            # Attempt to get the city by href, or create a new one if it doesn't exist
            farm, created = Farm.objects.get_or_create(
                href=row['href'], 
                city=city,
                image_url=row['image_url'],
                title=row['title']
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
