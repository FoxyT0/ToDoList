from django.db import models


class Task(models.Model):
    title = models.CharField('Name of task', max_length=30)
    text = models.TextField('Description of task')

    def __str__(self):
        return self.title
