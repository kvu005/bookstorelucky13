
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Authors(models.Model):
    Authorname = models.CharField(max_length =100)
    AuthorBio = models.TextField()

    def _str_(self):
        return self.Authorname

class Books(models.Model):
    Isbn = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length =100 )
    AuthorName = models.ForeignKey(Authors,related_name='author_detail', on_delete= models.CASCADE )
    Genere= models.CharField(max_length=100)
    PublishDate=models.CharField(max_length=4)
    Publisher = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CopiesSold= models.IntegerField()
    AvgRating= models.IntegerField()
    Description= models.TextField()

    class Meta:
        ordering = ['Isbn']
