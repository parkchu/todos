from django.db import models

class todos(models.Model):
    todo = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
