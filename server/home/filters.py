from django.db.models import Q

from django_filters import rest_framework as filters
from rest_framework import filters as rest_filter

from .models import Leads


class LeadsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="iexact")
    country = filters.CharFilter(lookup_expr="iexact")
    app_name = filters.CharFilter(lookup_expr="iexact")
    

    class Meta:
        model = Leads
        fields = ["name", "email", "country", "app_name"]