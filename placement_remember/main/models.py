from django.db import models

# Create your models here.

from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)