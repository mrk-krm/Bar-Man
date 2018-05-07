from rest_framework import serializers
from .models import Staff, Waiter, Orders,Items


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id','name', 'position')

class WaiterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ('id','name')


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id','waiter', 'table_no', 'total_cost')

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id','name','selling_price','buying_price','quantity')