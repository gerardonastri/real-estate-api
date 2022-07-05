from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    purpose = models.CharField(max_length=20, null=True, blank=True)
    minPrice = models.IntegerField(null=True, blank=True)
    maxPrice = models.IntegerField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    baths = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = JSONField()

    def __str__(self):
        return self.title


# class User(models.Model):
#     username = models.CharField(max_length=40)
#     password = models.CharField(max_length=300)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username
