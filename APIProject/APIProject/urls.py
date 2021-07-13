
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import routers, views
from api import views
router=routers.DefaultRouter()

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router.register("restraunt",views.RestrauntViewSet,basename="restraunt")
router.register("restrauntbank",views.RestrauntBankViewset,basename="restrauntbank")
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"),
    path('api/resfresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
  
]
