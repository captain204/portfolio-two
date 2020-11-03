from django.urls import path

from .views import HomePageView


urlpatteerns=[
    path('', HomePageView.as_view(),name='home')
]