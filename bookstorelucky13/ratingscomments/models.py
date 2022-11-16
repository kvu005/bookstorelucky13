from django.db import models

# Create your models here.

class Authors(models.Model):
    AuthorName = models.CharField(max_length=50)
    AuthorBio = models.TextField()

    def __str__(self):
        return self.AuthorName

class Books(models.Model):
    Isbn = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=100)
    AuthorName = models.ForeignKey(Authors, on_delete=models.CASCADE)
    Genre = models.CharField(max_length=50)
    PublishedDate = models.CharField(max_length=4)
    Publisher = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CopiesSold = models.IntegerField()
    AvgRating = models.IntegerField()
    Description = models.TextField()


    class Meta:
        ordering = ['Isbn']

class Users(models.Model):
    UserId = models.IntegerField(primary_key=True)
    UserName = models.TextField()
    Password = models.TextField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    HomeAddress = models.TextField()

    def __str__(self):
        return self.UserId
    
    class Meta:
        ordering = ['UserId']

class Comments(models.Model):
    CommentId = models.AutoField(primary_key=True)
    Comments = models.CharField(max_length=100)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    Isbn = models.ForeignKey(Books, on_delete=models.CASCADE)
    DateStamp = models.DateField()

    def __str__(self):
        return self.CommentId

    class Meta:
        ordering = ['CommentId']

class Ratings(models.Model):
    RatingId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    Isbn = models.ForeignKey(Books, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    DateStamp = models.DateField()

    def __str__(self):
        return self.RatingId

    class Meta:
        ordering = ['Rating']