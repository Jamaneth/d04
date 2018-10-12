from django.db import models

# Create your models here.
class Article(models.Model):

    css_style = models.CharField(max_length = 20)
    page_title = models.CharField(max_length = 100)
    content = models.TextField(null = True)

    def __str__(self):
        return self.page_title
