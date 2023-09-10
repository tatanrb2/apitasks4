from rest_framework import routers
from .api import StateViewSet, TaskViewSet

router = routers.DefaultRouter()

# Auto create the GET, POST, PUT, DELETE methods
router.register('api/states', StateViewSet, 'states')
router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls
