from django.db import models

from core.user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

"""
    General workplace structure:
        - name : string
        - image : picture
        - address : string
        - country : string
        - rating : int
        - price : float
        - publisher : User
        - creation datetime : datetime
        - modification datetime : datetime
        - description : string
"""
class Workplace(models.Model):
    # name
    name = models.CharField(max_length=32)

    # image, TODO
    image = models.ImageField()

    # address, TODO: use link instead
    address = models.CharField(max_length=64)

    # country, TODO: use link instead
    country = models.CharField(default='', max_length=32)

    # rating
    rating = models.IntegerField(default=0, 
                                 validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                    ]
                                 )
    
    # price
    price = models.FloatField(default=0,
                                validators=[
                                    MinValueValidator(0)
                                    ]
                              )

    # publisher
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    # creation
    creation_datetime = models.DateTimeField(auto_now_add=True)

    # modification
    modif_datetime = models.DateTimeField(auto_now=True)

    # description
    description = models.TextField(default='', blank=True)           # eventual comments

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    href = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name



class Farm(models.Model):
    title = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(default=None, max_length=200, blank=True)
    href = models.URLField(max_length=200, unique=True)
    # address = models.CharField(max_length=256, blank=True)
    # country = models.CharField(max_length=64, blank=True)
    # description = models.TextField(blank=True)
    # price = models.CharField(max_length=100, blank=True)  # Added price field as a CharField
    # publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    # creation_datetime = models.DateTimeField(auto_now_add=True)
    # modif_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Coworking(models.Model):
    title = models.CharField(max_length=100)
    href = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    starting_price = models.CharField(max_length=100, blank=True)  # Kept as CharField for flexibility
    image_url = models.URLField(default=None, max_length=200, blank=True)  # Added image_url field as a URLField

    def __str__(self):
        return self.title
