from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    something = models.CharField(max_length=10, default='hello')

    def __str__(self):
        return self.title