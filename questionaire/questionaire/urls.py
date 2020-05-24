"""questionaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView #one step view to skip email verification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),#login via browsable api
    path('api/rest-auth',include("rest-auth.urls")), #login via rest
    path('api/rest-auth/registration',include("rest-auth.registration.urls")), # reg via rest
    path("accounts/",include("django_registration.backends.one_step.urls")), #login  paths using browser
    path("accounts/register/", #reg  paths using browser
        RegistrationView.as_view(
        form_class=CustomUserForm,
        success_url="/",), name="django_registration_register")


]
