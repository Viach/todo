from django.db import models
import django.utils.timezone

class Task(models.Model):
    title = models.CharField(blank=False, max_length=500)
    body = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=django.utils.timezone.now)    