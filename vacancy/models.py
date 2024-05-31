from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Job(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    salary = models.IntegerField(default=0)
    company = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('FT', 'Полный рабочий день'),
            ('PT', 'Частичная занятость'),
            ('CT', 'Контракт'),
            ('FL', 'Фриланс'),
        ],
    )

class UsersJob(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)