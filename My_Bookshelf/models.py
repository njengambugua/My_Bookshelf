from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=30)
    summary = models.TextField()
    genre = models.CharField(max_length=20)
    publish_date = models.DateField()
