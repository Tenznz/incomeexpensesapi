from django.db import models


# Create your models here.

class Expense(models.Model):
    CATEGORY_OPTIONS = (
        ('ONLINE SERVICES', 'ONLINE SERVICES'),
        ('TRAVEL', 'TRAVEL'),
        ('FOOD', 'FOOD'),
        ('RENT', 'RENT'),
        ('OTHER', 'OTHER')
    )
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255, default="OTHER")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.CharField(max_length=255)
    owner = models.ForeignKey(to='authentication.User', on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False)
