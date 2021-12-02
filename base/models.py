from django.db import models
from django.contrib.auth.models import User

from base.views import taskList
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # dar nome ao objeto
    def __str__(self):
        return self.title

    # metadata para poder ordenar os itens
    class Meta:
        ordering = ['complete']
