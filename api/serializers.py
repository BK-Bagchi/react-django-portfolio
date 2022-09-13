from rest_framework import serializers
from django_portfolio.models import *


class SkillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillDetail
        fields = '__all__'


class AdditionalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalSkills
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
