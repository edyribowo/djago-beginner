from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core.views import TestView
from core import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('get_vaccine_data/', views.get_vaccine_data),
    path('photo_verification/', views.photo_verification)
]
