from django.db import models
import datetime as dt


class Task(models.Model):

    FAMILY = 'F'
    WORK = 'W'
    PERSONAL = 'P'
    
    TODO_CATEGORIES_CHOICES = (
            (FAMILY, 'Family'),
            (WORK, 'Work'),
            (PERSONAL, 'Personal'),
        )
    
    HIGH = 'H'
    NORMAL = 'N'
    LOW = 'L'
    
    TODO_PRIORITIES_CHOICES = (
            (HIGH, 'High'),
            (NORMAL, 'Normal'),
            (LOW, 'Low'),
        )

    title = models.CharField(blank=False, max_length=500)
    body = models.TextField(blank=True, default='')
    category = models.CharField(blank=True, choices=TODO_CATEGORIES_CHOICES, default=WORK, max_length=1)
    priority = models.CharField(blank=True, choices=TODO_PRIORITIES_CHOICES, default=NORMAL, max_length=1)
    should_do_before = models.DateField(default=dt.date.today)  
    done = models.BooleanField(blank=False, default=False)  
    created_at = models.DateField(default=dt.date.today)    