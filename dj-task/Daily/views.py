from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

from django.urls import reverse_lazy

from .decorators import unauthenticated_user
from .models import ToDoList
from .utils import * 
from .forms import * 


@login_required(login_url='login')
def MainPage(request):
    return render(request, 'Daily/home-page.html')


@login_required(login_url='login')
def home(request):
    do = ToDoList.objects.all()
    context = {'do': do}
    return render(request, 'Daily/home.html', context)



class ListDetail(ObjectDetailMixin, View):
    model = ToDoList
    template = 'Daily/detail_list.html'



class ListCreate(ObjectCreateMixin, View):
    form_model = ToDoListForm
    template = 'Daily/create_list.html'
    home = 'home'


class ListUpdate( ObjectUpdateMixin, View):
    model = ToDoList
    form_model = ToDoListForm
    template = 'Daily/update_list.html'
    home = 'home'


class ListDelete(ObjectDeleteMixin, View):
    model = ToDoList
    template = 'Daily/delete_list.html'
    redirect_url = 'home'

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home-page')

@unauthenticated_user
def registerPage(request):
   
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

