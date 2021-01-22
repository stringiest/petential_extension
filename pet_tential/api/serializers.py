from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'meal_type', 'date', 'fed_at', 'comment', 'treats')

class CreateFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('meal_type', 'date', 'comment', 'treats')