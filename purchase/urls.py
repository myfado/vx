from django.urls import path
from .views import *


app_name = 'purchase'

urlpatterns = [
    path('', PurchaseList.as_view(), name='purchase-list'),
    path('create/', PurchaseCreate.as_view(), name='purchase-create'),
    path('update/<int:pk>/', PurchaseUpdate.as_view(), name='purchase-update'),
    path('<int:pk>/', PurchaseDetail.as_view(),name='purchase-detail'),
    path('delete/<int:pk>/', PurchaseDelete.as_view(), name='purchase-delete'),

	]
