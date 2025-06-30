from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework import viewsets,permissions
from .serializers import *
from rest_framework.response import Response



class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset,many = True)
        return Response(serializer.data)

    def create(self, request):
        serialzer = self.serializer_class(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors,status =400)

    def retrieve(self, request, pk=None):
        schedule = self.queryset.get(pk = pk)
        serialzer = self.serializer_class(schedule)
        return Response(serialzer.data)

    def destroy(self, request, pk=None): 
        schedule = self.queryset.get(pk = pk)
        schedule.delete()
        return Response(status=204)
        
class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def list(self,request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset,many = True)
        return Response(serializer.data)
        
    
    def toggle(self,request,pk = None):
        status = self.queryset.get(pk = pk)
        serializer = self.serializer_class(status, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = 400)
        
    def retrieve(self,request,pk=None):
        status = self.queryset.get(pk = pk)
        serializer = self.serializer_class(status)
        return Response(serializer.data)
