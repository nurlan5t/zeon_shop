from rest_framework import serializers
from info.models import News, AboutUs, HelpQA, OurAdvantages


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
