from django.contrib import admin
from phonebox_plugin.models import Number


@admin.register(Number)
class NumPlanAdmin(admin.ModelAdmin):
    list_display = ("number", "tenant", "description", "provider", "forward_to")
