from django.urls import path

from . import views

urlpatterns = [
    path('', views.IncomeListAPIView.as_view(), name='income-list'),
    path('<int:id>', views.IncomeDetailsAPIView.as_view(), name='income-details')
]
