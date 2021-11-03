from django.urls import path, include
from rest_framework import routers

from .views import OprosAPIView, MatterAPIView, ResultOprosAPIView

router = routers.DefaultRouter()
router.register('opros', OprosAPIView, basename='opros_api')
router.register('matter', MatterAPIView, basename='matter_api')
router.register('result_opros', ResultOprosAPIView, basename='result_opros_api')

urlpatterns = router.urls
