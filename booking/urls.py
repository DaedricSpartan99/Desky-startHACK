from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='bookings'),
    #path('<int:booking_id>', views.booking, name='booking'),
    path('search/', views.get_queryset, name='search'),

]