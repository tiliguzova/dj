from django.urls import path

from info import views

urlpatterns = [
    path('', views.main, name="main"),
    path('all', views.read_pizza, name="read_pizza"),
    path('contest', views.contest, name="contest"),
]
