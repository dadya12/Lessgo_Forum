from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegistrationView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
]
