
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers, views
from api import views
router=routers.DefaultRouter()
router.register("Company",views.CompanyViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]
