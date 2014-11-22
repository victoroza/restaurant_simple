from rest_framework import serializers
from deli.models import Restaurant, FoodItem
import datetime


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'created', 'name', 'email', 'phone', 'address',
        'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'openTime', 'closeTime','foodItem')

class FoodItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'created', 'name', 'description', 'price', 'restaurant')