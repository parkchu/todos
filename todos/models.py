from django.db import models

class todos(models.Model):
    todo = models.CharField(max_length=100)
    finish = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.todo
