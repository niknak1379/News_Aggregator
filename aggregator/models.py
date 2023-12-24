from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.TextField()
    author = models.TextField()
    source = models.TextField()

    def __str__(self):
        return self.title
