from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Contact(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=True, blank=True)  # New email field
    #description = CKEditor5Field('Description', config_name='extends', default='')  # New CKEditor field

    def __str__(self):
        return f"{self.code} - {self.name}"

class TelephoneLine(models.Model):
    category = models.CharField(max_length=100)
    lines = models.TextField()

    def __str__(self):
        return self.category


class ContactInfo(models.Model):
    department = models.CharField(max_length=100)
    tasks = models.TextField()
    contact_number = models.CharField(max_length=45)

    def __str__(self):
        return self.department
