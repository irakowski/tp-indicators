from django.shortcuts import render
from django.views import generic
# Create your views here.
class TpForm(generic.TemplateView):
    template_name = 'records/form.html'
