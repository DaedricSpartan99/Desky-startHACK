# core/user/serializers.py
from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance


    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        representation = super().to_representation(instance)

        # Custom transformation example:
        representation['created'] = instance.created.strftime('%Y-%m-%d %H:%M:%S')
        representation['updated'] = instance.updated.strftime('%Y-%m-%d %H:%M:%S')
        
        # del representation['is_staff']

        return representation

    def to_internal_value(self, data):
        """
        Dict of primitive datatypes -> Object instance.
        """
        internal_value = super().to_internal_value(data)
        
        
        # Make sure to hash the password if it's being set
        password = data.get('password')
        if password:
            instance = self.Meta.model(**internal_value)
            instance.set_password(password)
            internal_value['password'] = instance.password

        return internal_value

    def create(self, validated_data):
        # Use the create_user method to handle password hashing
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Update user fields except for the password
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
