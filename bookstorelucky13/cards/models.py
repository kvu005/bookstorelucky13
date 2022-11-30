from datetime import date
from django.db import models
from users.models import User


class CreditCard(models.Model):
    YEAR_CHOICES = [(y, y)
                    for y in range(date.today().year, date.today().year+5)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cards")
    number = models.CharField(max_length=16)
    expiry_month = models.IntegerField(choices=MONTH_CHOICE)
    expiry_year = models.IntegerField(choices=YEAR_CHOICES)
    cvv = models.CharField(max_length=3)
