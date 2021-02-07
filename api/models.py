from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    dept = models.CharField(max_length=30)

    def __str__(self):
        return self.dept


class Skills(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    dept = models.ForeignKey(Category, on_delete=models.CASCADE)
    career = models.TextField(max_length=1000, blank=True, null=True)
    infla = models.TextField(max_length=1000, blank=True, null=True)
    dev = models.TextField(max_length=1000, blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    myself = models.CharField(max_length=300)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
