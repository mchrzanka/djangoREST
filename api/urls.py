from django.urls import path
from . import views

urlpatterns=[
    path('', views.apiOverview), #pass in the getData view
    path('item-list/', views.itemList), #pass in the getData view
    path('item-detail/<str:pk>/', views.itemDetail, name="item-detail"), #pass in the getData view
    path('item-create/', views.itemCreate, name="item-list"), #pass in the getData view
    path('item-update/<str:pk>/', views.itemUpdate), #pass in the getData view
    path('item-delete/<str:pk>/', views.itemDelete), #pass in the getData view
]