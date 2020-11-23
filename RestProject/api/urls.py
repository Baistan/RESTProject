from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',purchase_list,name='purchase'),
    path('purchase-list/',purchaseList,name='purchase-list'),
    # path('purchase-detail/<int:pk>/',purchaseDetailList,name='purchase-detail'),
    path('purchase-update/<int:pk>/',purchaseUpdate,name='purchase-update'),
    path('purchase-delete/<int:pk>/',purhaseDelete,name='purchase-delete'),
    path('purchase-create/<int:pk>/',purchaseCreate,name='purchase-create'),
    path('purchase-filter/',purchaseFilterList,name='purchaselist'),
    path('register/',accounRegister,name='register')
]