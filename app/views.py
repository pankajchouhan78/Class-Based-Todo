from django.shortcuts import render
from .form import CreateForm
from . models import *
from django.views.generic import CreateView, UpdateView,DeleteView
# Create your views here.

class index(CreateView):
    model = Todo
    form_class = CreateForm
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context
    
class update(UpdateView):
    model = Todo
    template_name = "update.html"
    success_url = "/"
    fields = {'title','completed'}

    
class delete(DeleteView):
    model = Todo
    template_name = "delete.html"
    success_url = "/"
    