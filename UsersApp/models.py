from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mail = models.CharField(unique=True, null=False, max_length=50)
    password = models.CharField(null=False, max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'