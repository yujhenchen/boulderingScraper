from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions', views.competitions, name='competitions'),
    path('athletes', views.athletes, name='athletes'),
    path('news', views.news, name='news')
]