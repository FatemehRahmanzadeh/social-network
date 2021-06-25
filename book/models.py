from django.db import models
from user.models import User
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    name = models.CharField('name', max_length=150, null=True)


class Book(models.Model):
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
    STATUS_CHOICE = [('F', 'Free'), ('B', 'Borrowed'), ('D', 'Deprecated')]
    title = models.CharField('book title', max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publish_year = models.DateTimeField('publish_year', null=True)
    record_date = models.DateTimeField('release_year', null=True, auto_now_add=True)
    update_time = models.DateTimeField('update time', auto_now=True)
    book_info = models.TextField('book information', null=True, blank=True)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICE, default='F')

    def change(self):
        """
        changes the status of book
        """

        if self.status == 'F':
            self.status = 'B'

        else:
            self.status = 'F'
        self.save()

        return self.status

    def get_publish_year(self):
        return self.publish_year.year

    def __str__(self):
        return f'title:{self.title}\nauthor(s):{self.author}'
