from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [
    path('', CustomerList.as_view(), name='customer-list'),
    path('create/', CustomerCreate.as_view(), name='customer-create'),
    path('update/<int:id>/', CustomerUpdate.as_view(), name='customer-update'),
    path('<int:pk>/', CustomerDetail.as_view(),name='customer-detail'),
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='customer-delete'),

	]
