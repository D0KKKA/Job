from django.shortcuts import render
from rest_framework import viewsets
from vacancy import models, serializers
# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer

class UsersJobViewSet(viewsets.ModelViewSet):
    queryset = models.UsersJob.objects.all()
    serializer_class = serializers.UsersJobSerializer