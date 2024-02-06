from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    #needs two things at minimum, the model we want to serialize and the fields we want to see.
    class Meta:
        model = Item
        fields = '__all__'