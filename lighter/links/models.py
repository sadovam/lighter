from django.db import models
from django.utils import timezone

class LinkPage(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class LinkGroup(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    note = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    page = models.ForeignKey(LinkPage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Link(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=255)
    note = models.TextField(blank=True)
    add_date = models.DateTimeField('Add Date', default=timezone.now)
    is_public = models.BooleanField(default=True)
    group = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
