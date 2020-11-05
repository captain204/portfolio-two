from django.urls import path

from .views import HomePageView,CreateContactView


urlpatterns=[
    path('', CreateContactView.as_view(),name='home'),
]