from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from rest_framework.routers import DefaultRouter

from search import views as search_views

from home import views as home_views
from django.views.generic.base import RedirectView

public_router = DefaultRouter()
public_router.register(r"leads", home_views.LeadsApiViewset, "public_leads_api")


urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', RedirectView.as_view(url='https://docs.google.com/forms/d/e/1FAIpQLSe20ouSBwFmAg7uZuM_xHT_nvznQKemyPeNCzqC9lG1gujCkQ/viewform', permanent=True), name='root-redirect'),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path("staff/", include('staff.urls', namespace="staff")),

    path('search/', search_views.search, name='search'),
    # path('proxy/trust-pilot/', home_views.ProxyView.as_view(), name='proxy_view'),
    path('redirect/', home_views.ForceRedirectionView.as_view(), name='force-redirection-view'),
    path('central/redirect/', home_views.CentralRedirectionView.as_view(), name='central-redirection-view'),
    path('my/country/', home_views.CountryApi.as_view(), name='country_api'),
    path('country/phone/', home_views.PhoneCodesByCountryApi.as_view(), name='phone_code_by_country_api'),
    path('signup/complete/', home_views.ThankYouView.as_view(), name='thankyou_view'),
    path("api/v1/public/", include(public_router.urls)),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
]
