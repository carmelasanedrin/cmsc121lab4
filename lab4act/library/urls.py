from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('updatebooks/<str:pk>', views.updatebooks, name='updatebooks'),
    path('deletebook/<str:pk>', views.deletebook, name='deletebook'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('updateauthor/<str:pk>', views.updateauthor, name='updateauthor'),
    path('deleteauthor/<str:pk>', views.deleteauthor, name='deleteauthor')

]
