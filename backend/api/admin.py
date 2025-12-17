"""Admin configuration for API models."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin interface for Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
