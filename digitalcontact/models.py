from django.db import models

class Contact(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.code} - {self.name}"

