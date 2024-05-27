from django.db import models
import datetime


class RoboData(models.Model):
    STATUS_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
    ]

    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.status}'


