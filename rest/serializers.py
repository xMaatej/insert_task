from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
from rest.models import Offer, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ['title', 'description', 'price', 'created', 'category']