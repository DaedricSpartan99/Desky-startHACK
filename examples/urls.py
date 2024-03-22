from django.urls import path, re_path
from transactions import views

# re_path (?P<name>pattern)
# start with ^
# end with $

urlpatterns = [
    path('', views.transactions_list),
    path('<int:pk>/', views.transaction_detail),
    re_path(r'^range/(?P<start>\d{4}-\d{2}-\d{2})to(?P<end>\d{4}-\d{2}-\d{2})/$', views.local_transaction_range),
    path('bonds/freq/<int:number>/', views.bond_list),
    path('bonds/', views.bond_list_all),
    path('brokers/', views.broker_list_all),
    path('currencies/', views.currency_list_all),
    path('blotup/', views.BlotUploadView.as_view(), name='upload-blot'),
    path('positioning/', views.get_positioning, name='positioning')
]
