from pyexpat import model
from django.db import models

# Create your models here.
class Authors(models.Model):
    AuthorName = models.CharField(max_length=100, primary_key=True)
    AuthorBio = models.TextField()
    Publisher = models.CharField(max_length=100)
    
    def __str__(self):
        return self.authorName

class Books(models.Model):
    Isbn = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=100)
    AuthorName = models.ForeignKey(Authors, to_field="AuthorName", db_column="AuthorName", on_delete=models.CASCADE)
    Genre = models.CharField(max_length=50)
    PublishedDate = models.CharField(max_length=4)
    Publisher = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CopiesSold = models.IntegerField()
    AvgRating = models.IntegerField()
    Description = models.TextField()

    class Meta:
        ordering = ['Isbn']