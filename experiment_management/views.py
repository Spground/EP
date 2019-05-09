from django.shortcuts import render
from django.http import HttpResponse
from experiment_management import models
from rest_framework import viewsets
from experiment_management import serializers


# Create your views here.
class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = models.Experiment.objects.all().order_by('-create_dt')
    serializer_class = serializers.ExperimentSerializer


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = models.Config.objects.all().order_by('-create_dt')
    serializer_class = serializers.ConfigSerializer

class ExperimentGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ExperimentGroup.objects.all().order_by('-create_dt')
    serializer_class = serializers.ExperimentGroupSerializer
