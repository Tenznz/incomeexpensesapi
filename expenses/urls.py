from django.urls import path

from . import views

urlpatterns = [
    path('', views.ExpensesListAPIView.as_view(), name='expenses-list'),
    path('<int:id>', views.ExpensesDetailsAPIView.as_view(), name='expenses-details')
]
