from rest_framework import serializers
from vacancy import models


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Job
        fields="__all__"

class UsersJobSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UsersJob
        fields="__all__"