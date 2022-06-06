from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login',views.LoginAPI.as_view(),name='login'),
    path('email-verify', views.VerifyEmail.as_view(), name='email-verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
