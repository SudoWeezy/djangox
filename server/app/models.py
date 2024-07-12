from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Participant(models.Model):
    class Status(models.TextChoices):
        IN = "IN", _("In")
        OUT = "OU", _("Out")
        CHECK = "CH", _("Check")

    name = models.CharField(max_length=50)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.IN,
    )
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    participants =  models.ManyToManyField('Participant')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title