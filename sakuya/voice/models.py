from django.db import models
from django.utils.timezone import now

from sakuya.accounts.models import Child


class Word(models.Model):
    lemma = models.CharField(max_length=30, blank=True)
    pron = models.CharField(max_length=30, blank=True)
    base = models.CharField(max_length=30, blank=True)
    pos1 = models.CharField(max_length=30, blank=True)
    pos2 = models.CharField(max_length=30, blank=True)
    pos3 = models.CharField(max_length=30, blank=True)
    conj_type = models.CharField(max_length=30, blank=True)
    conj_form = models.CharField(max_length=30, blank=True)
    tag = models.CharField(max_length=30, blank=True)
    
    date = models.DateTimeField('creation date', default=now, blank=True)
    owner = models.ForeignKey(Child)

    def __str__(self):
        return self.lemma + '(' + self.pos1 + ')'
