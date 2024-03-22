from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to trigger the sending of an email
    path('send-email/', views.trigger_email_view, name='send_email'),
]
