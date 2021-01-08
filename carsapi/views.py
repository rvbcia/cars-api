from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import CarSerializer, CarRateSerializer
from .models import Car, CarRate


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    #
    # @staticmethod
    # def get(request, format=None):
    #     products = Car.objects.all()
    #     serializer = CarSerializer(products, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = CarSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateView(generics.ListCreateAPIView):
    queryset = CarRate.objects.all()
    serializer_class = CarRateSerializer
