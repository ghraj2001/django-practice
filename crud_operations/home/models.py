from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=220)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.name

