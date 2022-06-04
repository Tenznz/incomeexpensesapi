from django.db import models


class Income(models.Model):
    SOURCE_OPTIONS = (
        ('SALARY', 'SALARY'),
        ('BUSINESS', 'BUSINESS'),
        ('SIDE-HUSTLES', 'SIDE-HUSTLES'),
        ('OTHERS', 'OTHERS')
    )
    source = models.CharField(choices=SOURCE_OPTIONS, max_length=255, default="OTHERS")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.CharField(max_length=255)
    owner = models.ForeignKey(to='authentication.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, null=False, blank=False)
