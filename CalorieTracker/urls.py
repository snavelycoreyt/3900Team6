from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


app_name = "Calorie Tracker"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

]

