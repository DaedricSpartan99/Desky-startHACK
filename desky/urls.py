"""
URL configuration for desky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from core.views import front
from booking.views import WorkplaceListCreateAPIView, WorkplaceDetailAPIView


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('rest-admin/', include(router.urls)),
    path("admin/", admin.site.urls),
    path('', front, name="front"),
    path('api/', include(('core.routers', 'core'), namespace='core-api')),
    path('booking/', include('booking.urls')),
    path('emailrequest/', include('emailrequest.urls')),
    #path('workplaces/', WorkplaceListCreateAPIView.as_view(), name='workplace-list'),
    #path('workplaces/<int:pk>/', WorkplaceDetailAPIView.as_view(), name='workplace-detail'),
    #path('social/', include('social.urls')),
    #path('booking/', include('booking.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += router.urls
