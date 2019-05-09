from django.db import models


# Create your models here.
class BaseModel(models.Model):
    create_dt = models.DateTimeField('create date', auto_now_add=True)
    update_dt = models.DateTimeField('update date', auto_now=True)
    description = models.CharField(max_length=2000)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class ExperimentGroup(BaseModel):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Experiment(BaseModel):
    experiment_group = models.ForeignKey(ExperimentGroup,
                                         related_name='experiments',
                                         on_delete=models.DO_NOTHING)


class Model(BaseModel):
    name = models.CharField(max_length=2000)
    source_file_path = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Config(BaseModel):
    config_json = models.CharField(max_length=10000)
    experiment = models.ForeignKey(Experiment, on_delete=models.DO_NOTHING)


class ExperimentRecord(BaseModel):
    experiment = models.ForeignKey(Experiment, on_delete=models.DO_NOTHING)
    config = models.ForeignKey(Config, on_delete=models.DO_NOTHING)
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING)


class ExperimentLog(BaseModel):
    info = models.CharField(max_length=2000)


class ExperimentEnviroment(BaseModel):
    software_info = models.CharField(max_length=2000)
    hardware_info = models.CharField(max_length=2000)

