from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    phone =models.CharField(max_length=12)
    desc= models.TextField()
    date = models.DateField()
   #objects = models.Manager()

    def __str__(self) -> str:
        return self.name