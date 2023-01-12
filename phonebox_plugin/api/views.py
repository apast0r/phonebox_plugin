from rest_framework.routers import APIRootView
from .. import filters
from ..models import Number
from . import serializers
from nautobot.core.api.views import ModelViewSet


class PhoneBoxPluginRootView(APIRootView):
    """
    phonebox_plugin API root view
    """
    def get_view_name(self):
        return 'PhoneBox'


class NumberViewSet(ModelViewSet):
    queryset = Number.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.NumberSerializer
    filterset_class = filters.NumberFilterSet
