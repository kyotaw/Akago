from django.db import models
from django.utils.timezone import now

from sakuya.accounts.models import Child


class Muscle(models.Model):
    strength = models.FloatField(default=-1.0, blank=True) 
    date = models.DateTimeField('creation date', default=now, blank=True)
    owner = models.ForeignKey(Child)
