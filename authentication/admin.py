from django.contrib import admin

# Register your models here.
from expenses.models import Expense

admin.site.register(Expense)
