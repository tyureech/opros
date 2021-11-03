from django.urls import path, include
from rest_framework import routers

from .views import OprosAPIView, MatterAPIView

router = routers.DefaultRouter()
router.register('opros', OprosAPIView, basename='opros')
router.register('matter', MatterAPIView, basename='matter')

urlpatterns = router.urls
