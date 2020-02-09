from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from .models import User

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name',
            'address', 'city', 'state', 'country', 'zip_code', 'phone',
            'website')
        read_only_fields = ('email',)

class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=15, required=True)
    website = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=200, required=True)
    city = serializers.CharField(max_length=100, required=True)
    state = serializers.CharField(max_length=100, required=True)
    country = serializers.CharField(max_length=100, required=True)
    zip_code = serializers.CharField(max_length=10, required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'phone': self.validated_data.get('phone', ''),
            'website': self.validated_data.get('website', ''),
            'address': self.validated_data.get('address', ''),
            'city': self.validated_data.get('city', ''),
            'state': self.validated_data.get('state', ''),
            'country': self.validated_data.get('country', ''),
            'zip_code': self.validated_data.get('zip_code', ''),
        })
        return data
