from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

]