from rest_framework import serializers
from core.user.models import User
from .models import City, Workplace, Farm, Coworking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include the fields you want to serialize for the User

class WorkplaceSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(read_only=True)  # Nested serialization for the publisher

    class Meta:
        model = Workplace
        fields = [
            'id',
            'name',
            'image',
            'address',
            'country',
            'rating',
            'price',
            'publisher',
            'creation_datetime',
            'modif_datetime',
            'description',
        ]
        read_only_fields = ['creation_datetime', 'modif_datetime']
    
    def create(self, validated_data):
        # You can add custom creation logic here if needed
        workplace = Workplace.objects.create(**validated_data)
        return workplace

    def update(self, instance, validated_data):
        # Custom update logic, excluding read-only fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class CitySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(default='city')
    class Meta:
        model = City
        fields = ['id', 'name', 'href', 'category']


class FarmSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(default='farm')
    city_name = serializers.CharField(source='city.name')
    class Meta:
        model = Farm
        fields = [
            'id',
            'title',
            'city',
            'city_name',
            'image_url',
            'href',
            'category'
        ]

class CoworkingSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(default='coworking')
    class Meta:
        model = Coworking
        fields = [
            'id',
            'title',
            'href',
            'description',
            'starting_price',
            'image_url',
            'category'
        ]

