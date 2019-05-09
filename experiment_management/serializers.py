from experiment_management import models
from rest_framework import serializers


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiment
        fields = ('id', 'experiment_group', 'create_dt',
                  'update_dt', 'description')


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Config
        fields = ('id', 'experiment', 'config_json', 'create_dt',
                  'update_dt', 'description')


class ExperimentGroupSerializer(serializers.ModelSerializer):

    experiments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.ExperimentGroup
        fields = '__all__'
