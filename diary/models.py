from django.db import models

# Create your models here.


class Diary(models.Model):
    body = models.CharField(max_length=108)

    def __str__(self):
        return self.body
