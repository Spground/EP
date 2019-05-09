from rest_framework import routers
from experiment_management import views

router = routers.DefaultRouter()
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'configs', views.ConfigViewSet)
router.register(r'experiment_groups', views.ExperimentGroupViewSet)

urlpatterns = router.urls

