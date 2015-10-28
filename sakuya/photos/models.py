from django.db import models
from django.utils.timezone import now
from sakuya.accounts.models import Child


class Stamp(models.Model):
    title = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='photos/stamps', blank=True)

    def __str__(self):
        return self.title
    

class Photo(models.Model):
    title = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='photos', blank=True)
    audio = models.FileField(upload_to='audio', blank=True)
    movie = models.FileField(upload_to='movies', blank=True)
    date = models.DateTimeField('creation date', default=now, blank=True)
    age = models.CharField(max_length=30)
    comment = models.CharField(max_length=30, blank=True)
    owner = models.ForeignKey(Child)
    stamp = models.ForeignKey(Stamp, blank=True, null=True)
    footer = models.CharField(max_length=30, blank=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
