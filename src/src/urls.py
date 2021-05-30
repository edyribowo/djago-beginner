from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('get_vaccine_data/', views.get_vaccine_data),
    path('photo_verification/', views.photo_verification),
    path('add_data_vaccine/', views.add_data_vaccine),
    path('update_vaccine_data/', views.update_vaccine_data),
    path('delete_vaccine_data/', views.delete_vaccine_data),
    path('verification_account_using_nik/', views.verification_account_using_nik)
]
