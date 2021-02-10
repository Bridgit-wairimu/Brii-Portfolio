from django.db import models
import datetime as dt 
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
        title = models.CharField(max_length=200)
        description = models.CharField(max_length=200, null=True, blank=True)
        created = models.DateTimeField(auto_now_add=True)
        tag = models.ForeignKey('Tag',on_delete=models.CASCADE, default=20)
        image = models.ImageField(upload_to='media/',default='default.jpg', blank=True,null=True)


        def __str__(self):
            return self.title


        def get_absolute_url(self):
            return reverse('index')


        @classmethod
        def all_image(cls):
            return cls.objects.all()

        def save_image(self):
            self.save()


class Tag(models.Model):
        name = models.CharField(max_length=200)

        def __str__(self):
            return self.name
