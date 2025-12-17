"""Serializers for API models."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Meta configuration for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
