from django.db import models

# Create your models here.

class Articls(models.Model):
    title = models.CharField('название', max_length=250)
    text_state = models.TextField('название')

    def __str__(self):
        return self.title