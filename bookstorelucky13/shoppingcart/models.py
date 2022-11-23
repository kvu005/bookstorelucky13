from pyexpat import model
from django.db import models

# Create your models here.
class shopping_cart(models.Model):
    user_ID = models.IntegerField()
    sc_ID = models.IntegerField(primary_key = True)
    isbn = models.IntegerField()
    book_title = models.CharField(max_length = 100)

    class Meta:
        ordering = ['sc_ID']
