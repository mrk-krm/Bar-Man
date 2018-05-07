from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Staff, Waiter, Orders,Items
from .serializers import StaffSerializers, WaiterSerializers, OrdersSerializers,ItemsSerializers

# Create your views here.

class StaffList(APIView):
    def get(self, request, format=None):
        my_staff = Staff.objects.all()
        serializers = StaffSerializers(my_staff, many=True)
        return Response(serializers.data)

class WaitersList(APIView):
    def get(self, request, format=None):
        waiters = Waiter.objects.all()
        serializers = WaiterSerializers(waiters, many=True)
        return Response(serializers.data)

class ItemsList(APIView):
    def get(self, request, format=None):
        items = Items.objects.all()
        serializers = ItemsSerializers(items, many=True)
        return Response(serializers.data)

class OrdersList(APIView):
    def get(self, request, format=None):
        orders = Orders.objects.all()
        serializers = OrdersSerializers(orders, many=True)
        return Response(serializers.data)