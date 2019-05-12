from experiment_management import models
from rest_framework import viewsets
from experiment_management import serializers


class FilterMixin:
    '''可以过滤某些字段的Mixin, 貌似必须放在最左边'''
    queryset = None
    query_filter_fields = None

    def get_queryset(self):
        assert self.queryset is not None
        args = {}
        for field in self.query_filter_fields:
            field_value = self.request.query_params.get(field, None)
            if field_value is not None:
                args[field] = field_value
        return self.queryset.filter(**args)


# Create your views here.
class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = models.Experiment.objects.all().order_by('id')
    serializer_class = serializers.ExperimentSerializer


class ConfigViewSet(FilterMixin, viewsets.ModelViewSet):
    queryset = models.Config.objects.all().order_by('id')
    serializer_class = serializers.ConfigSerializer
    query_filter_fields = ['experiment', ]


class ExperimentGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ExperimentGroup.objects.all().order_by('id')
    serializer_class = serializers.ExperimentGroupSerializer


class ExperimentLogViewSet(viewsets.ModelViewSet):
    queryset = models.ExperimentLog.objects.all().order_by('id')
    serializer_class = serializers.ExperimentLogSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = models.Model.objects.all().order_by('id')
    serializer_class = serializers.ModelSerializer


class ExperimentRecordViewSet(FilterMixin, ModelViewSet):
    serializer_class = serializers.ExperimentRecordSerializer
    queryset = models.ExperimentRecord.objects.all().order_by('id')
    query_filter_fields = ['experiment', ]


class ExperimentEnviromentViewSet(viewsets.ModelViewSet):
    queryset = models.ExperimentEnvironment.objects.all().order_by('id')
    serializer_class = serializers.ExperimentEnvironmentSerializer
