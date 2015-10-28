from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Medal(models.Model):
    title = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='accounts/medals', blank=True)


class Child(models.Model):
    name = models.CharField(max_length=30, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    birth = models.DateTimeField('birth day', blank=True)
    image = models.ImageField(upload_to='accounts/children', blank=True)
    comment = models.CharField(max_length=140, blank=True)
    medals = models.ManyToManyField(Medal, blank=True)
    parent = models.ForeignKey(User, default=1, null=True)

    def detail_age(self):
        postnatal = now() - self.birth
        years = postnatal.days // 365
        months = (postnatal.days - 365 * years) // 31
        days = postnatal.days - 365 * years - 31 * months
        return str(years) + '歳' + str(months) + 'ヶ月' + str(days) + '日'

    def __str__(self):
        return self.name
