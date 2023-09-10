# Used to convert python code in JSON or XML

from rest_framework import serializers
from .models import State, Task


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'state', 'created_at')
        read_only_fields = ('created_at', )
