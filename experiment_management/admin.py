from django.contrib import admin
from experiment_management.models import (Experiment, ExperimentGroup,
                                          ExperimentRecord, ExperimentLog,
                                          Config, Model, ExperimentEnvironment)
# Register your models here.

admin.site.register(Experiment)
admin.site.register(ExperimentGroup)
admin.site.register(ExperimentRecord)
admin.site.register(ExperimentLog)
admin.site.register(Config)
admin.site.register(Model)
admin.site.register(ExperimentEnvironment)
