import simplejson
import json
import requests
import time

from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.conf import settings
from django.contrib.auth import login, logout

from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .phone_code import phone_codes
from .utils import get_country_code_from_ip

from .models import *
from .filters import LeadsFilter
from .permissions import LeadsPermission
from .serializers import LeadsSerializer


class ForceRedirectionView(View):
    template_name = "home/force-redirection/force-redirection.html"

    def get(self, request):
        
        red_url = request.GET.get("red_url")
        # if red_url:
        #     time.sleep(10)
        #     return redirect(red_url)
        # else:
        if not red_url:
            raise Http404

        variables = {

        }

        return render(request, self.template_name, variables)


class ProxyView(View):
    template_name = "home/proxy/index.html"

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)


class CountryApi(APIView):
    def get(self, request):
        r = requests.get("http://ip-api.com/json")
        json_data = json.loads(r.content.decode('utf-8'))
        return Response(json_data)


class PhoneCodesByCountryApi(APIView):
    def get(self, request):
        country = request.GET.get("country")
        c = phone_codes.get(country)
        return Response({
            "phone_code": c
        })


class CentralRedirectionView(View):
    template_name = "home/central-redirection/central-redirection.html"

    def get(self, request):
        main = request.GET.get("main")
        # ip = get_client_ip(request)
        # country_code = get_country_code_from_ip(ip)

        try:
            obj = CentralRedirection.objects.get(accepted_param=main, is_active=True)
            variables = {
                "obj": obj,
            }
            return render(request, self.template_name, variables)
        except:
            raise Http404



class LeadsApiViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    {
        "name": "amir",
        "email": "amir1@gmail.com",
        "phone": "01623539982",
        "country": "Bangladesh",
        "app_name": "test"
    }
    """
    serializer_class = LeadsSerializer
    queryset = Leads.objects.all()
    permission_classes = (IsAuthenticated, LeadsPermission)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LeadsFilter


class ThankYouView(View):
    template_name = "home/thank-you.html"

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)