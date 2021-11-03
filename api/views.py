from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from opros.models import MatterModel, OprosModel
from .serializers import MatterSerializer, OprosSerializer


class MatterAPIView(ModelViewSet):
    queryset = MatterModel.objects.all()
    serializer_class = MatterSerializer


class OprosAPIView(ModelViewSet):
    queryset = OprosModel.objects.all()
    serializer_class = OprosSerializer