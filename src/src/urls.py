from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Vaccine KIT API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # url('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('get_vaccine_data/', views.get_vaccine_data),
    path('photo_verification/', views.photo_verification),
    path('add_data_vaccine/', views.add_data_vaccine),
    path('update_vaccine_data/', views.update_vaccine_data),
    path(r'delete_vaccine_data/(?P<nik>\w+)/$', views.delete_vaccine_data),
    path('verification_account_using_nik/', views.verification_account_using_nik),

    path('get_vaccine_data_email/', views.get_vaccine_data_email),
    path('get_vaccine_data_barcode/', views.get_vaccine_data_barcode)
]
