from rest_framework import routers
from experiment_management import views

router = routers.DefaultRouter()
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'configs', views.ConfigViewSet, basename=r'configs')
router.register(r'experiment_groups', views.ExperimentGroupViewSet)
router.register(r'experiment_records', views.ExperimentRecordViewSet,
                basename=r'experiment_records')
router.register(r'experiment_logs', views.ExperimentLogViewSet)
router.register(r'experiment_environments', views.ExperimentEnviromentViewSet)
router.register(r'models', views.ModelViewSet)

urlpatterns = router.urls
