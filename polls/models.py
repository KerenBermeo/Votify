from django.contrib.auth.models import User
from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Option(models.Model):
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='votes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'option')
