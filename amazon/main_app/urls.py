from django.urls import path

from . import views
from .views import ReviewListView

urlpatterns = [
    #path('', views.index, name='index'),
    path('', ReviewListView.as_view(), name='article-list'),
]