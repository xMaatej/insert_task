from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
from rest.models import Offer, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
