from django.urls import path

from .views import HomePageView,CreateContactView


urlpatterns=[
    path('', HomePageView.as_view(),name='home'),
    path('contact/', CreateContactView.as_view(), name='home'),
]