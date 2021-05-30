from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    # title = models.CharField(max_length=100)
    # description = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    nik = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    photo = models.TextField(null=True)
    ttl = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    vaccineStatus = models.CharField(max_length=100, null=True)
    firstVaccineDate = models.CharField(max_length=100, null=True)
    secondVaccineDate = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

