from django.db import models
from user.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField('book title', max_length=150)
    authors = models.CharField('authors', max_length=150)
    release_year = models.CharField('release_year',max_length=4, null=True)
    update_time = models.DateTimeField('update time', auto_now_add=True)
    book_info = models.TextField('book information', null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
