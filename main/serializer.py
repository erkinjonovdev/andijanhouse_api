from rest_framework import serializers
from .models import Information, Banner, PaymentOptions, Advertising, ContactUs, Company, Complex, Services, \
    WhyRealtor, Realtors, HowWorks


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Information
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        fields = '__all__'


class PaymentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = PaymentOptions
        fields = '__all__'


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Advertising
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ContactUs
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Company
        fields = '__all__'


class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Complex
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Services
        fields = '__all__'


class WhyRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = WhyRealtor
        fields = '__all__'


class RealtorsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Realtors
        fields = '__all__'


class HowWorksSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = HowWorks
        fields = '__all__'
