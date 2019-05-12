from experiment_management import models
from rest_framework import serializers


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiment
        fields = '__all__'


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


class ExperimentLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExperimentLog
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Model
        fields = '__all__'


class ExperimentRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExperimentRecord
        fields = '__all__'


class ExperimentEnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExperimentEnvironment
        fields = '__all__'
