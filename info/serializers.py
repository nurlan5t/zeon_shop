from rest_framework import serializers
from info.models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage, \
    PublicOffer, CallBack
from phonenumber_field.serializerfields import PhoneNumberField

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class HelpQASeralizer(serializers.ModelSerializer):
    class Meta:
        model = HelpQA
        fields = '__all__'


class OurAdvantagesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = '__all__'


class SliderMainPageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = SliderMainPage
        fields = '__all__'


class PublicOfferSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = ('user_name', 'user_phone', 'type_of_treatment')
