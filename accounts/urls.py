from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
    # path('register/', auth_views.LoginView.as_view(
    #     template_name='auth/registration.html'
    # ), name='register'),
        path("signup/", SignUpView.as_view(template_name='auth/registration.html'), name="signup"),


]
    