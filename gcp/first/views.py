from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import HelloSerializer
from rest_framework.response import Response 
from django.http import HttpResponse

class HelloView(APIView):
    def get(self, request):
        serializer = HelloSerializer()
        return HttpResponse("Hello")