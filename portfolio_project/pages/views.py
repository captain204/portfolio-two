from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView




class HomePageView(TemplateView):
    template_name = 'home.html'


class CreateContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name ='home.html'
    success_url = 'contact'
    success_message = "%(message_field)s I 'll get back to you shortly"
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
        cleaned_data,
        message_field="Thanks you for reaching out",
    )
    
    def form_valid(self,form):
        return super().form_valid(form)




