from django.urls import path 
from django.contrib.auth import views as auth_views


from .views import *


urlpatterns = [
    path('', MainPage, name='home-page'),
    path('home/', home, name='home'),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), 
        name='reset_password'),

    path('reset_password_sent/', 
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/passwor_reset_sent.html'),
        name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset_confirm'),
    
    path('reset_password_complete/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_complete'),

        path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'),
        name='password_change'),


    path('create/', ListCreate.as_view(), name="create_list"),
    path('detail/<str:slug>/', ListDetail.as_view(), name='detail_list'),
    path('<str:slug>/update/', ListUpdate.as_view(), name='update_list'),
    path('<str:slug>/delete/', ListDelete.as_view(), name='delete_list'),
]