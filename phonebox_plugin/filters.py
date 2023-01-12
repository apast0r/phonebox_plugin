import django_filters
from django.db.models import Q
from nautobot.circuits.models import Provider
from nautobot.dcim.models import Region, Site
from nautobot.tenancy.models import Tenant
from nautobot.utilities.filters import BaseFilterSet
from nautobot.utilities.filters import TagFilter
from phonebox_plugin.models import Number, VoiceCircuit


class NumberFilterSet(BaseFilterSet):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    number = django_filters.ModelMultipleChoiceFilter(
        field_name='number',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='number',
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='region__id',
        to_field_name='id',
        label='Region (id)',
    )
    provider = django_filters.ModelMultipleChoiceFilter(
        queryset=Provider.objects.all(),
        field_name='provider__id',
        to_field_name='id',
        label='Region (id)',
    )
    forward_to = django_filters.ModelMultipleChoiceFilter(
        field_name='forward_to',
        queryset=Number.objects.all(),
        to_field_name='number',
        label='forward_to',
    )
    tag = TagFilter()

    class Meta():
        model = Number
        fields = ('number',)

    def search(self, queryset, number, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(number__icontains=value)
        )


class VoiceCircuitFilterSet(BaseFilterSet):

    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    name = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        queryset=VoiceCircuit.objects.all(),
        to_field_name='name',
        label='name',
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name='tenant__id',
        to_field_name='id',
        label='Tenant (id)',
    )
    site = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        field_name='site__id',
        to_field_name='id',
        label='Site (id)',
    )
    region = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='region__id',
        to_field_name='id',
        label='Region (id)',
    )
    provider = django_filters.ModelMultipleChoiceFilter(
        queryset=Provider.objects.all(),
        field_name='provider__id',
        to_field_name='id',
        label='Provider (id)',
    )
    tag = TagFilter()

    class Meta():
        model = VoiceCircuit
        fields = ('name',)

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
        )
