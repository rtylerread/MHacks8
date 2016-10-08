from __future__ import unicode_literals
from django.db import models

class url_to_ping(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=200)
    twitter_id = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    def __int__(self):
        return self.twitter_id

# Create your models here.
