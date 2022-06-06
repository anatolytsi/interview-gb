from django.db import models


class SiteVisit(models.Model):
    ip = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now=True)
