from django.urls import path
from . import views

urlpatterns = [
    path('<str:page_view>/', views.page_view, name='page_view'),
    path('', views.index, name='index'),
]