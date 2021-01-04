from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View 
from django.http import HttpResponse
from .models import * 


class ObjectDetailMixin:
    model = None 
    template = None 

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template, context)


class ObjectCreateMixin:
    form_model = None 
    template = None 
    home = None 

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form':form})
    
    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(self.home)
        return render(request, self.template, context={'form': bound_form})


class ObjectDeleteMixin:
    model = None 
    template = None 
    redirect_url = None 

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        if request.user == obj.user:
            ToDoList.objects.filter(slug__iexact=slug).delete()
            return redirect(reverse(self.redirect_url))
        else:
            return HttpResponse('FORBIDDEN')


class ObjectUpdateMixin:
    model = None 
    form_model = None 
    template = None 
    home = None 


    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        if request.user == obj.user:
            if bound_form.is_valid():
                new_obj = bound_form.save()
                return redirect(self.home)
            return render(request, self.template, context={'form':bound_form, self.model.__name__.lower(): obj})
        else:
            return HttpResponse('FORBIDDEN')
