from django.urls import path
from .views import *


app_name = 'sell'

urlpatterns = [
    path('', SellList.as_view(), name='sell-list'),
    path('active/', SellItemList.as_view(), name='active-list'),
    path('create/', SellCreate.as_view(), name='sell-create'),
    path('update/<int:pk>/', SellUpdate.as_view(), name='sell-update'),
    path('<int:pk>/', SellDetail.as_view(),name='sell-detail'),
    path('delete/<int:pk>/', SellDelete.as_view(), name='sell-delete'),

	]
