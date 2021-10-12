from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LadyPCDetailSerializer
from .models import LadyPCDetail

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'years_active': 10
        }
        return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = LadyPCDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)