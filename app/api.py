from .models import State, Task
from rest_framework import viewsets, permissions
from .serializers import StateSerializer, TaskSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [permissions.AllowAny]   # In the future, only admin users
    serializer_class = StateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]   # Any client can request the data
    serializer_class = TaskSerializer
