# digitallogs/models.py

from django.db import models

class Downtime(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    IMPACT_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    sn = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    system_channel_name = models.CharField(max_length=255)
    reason = models.TextField()
    downtime_total_time = models.DurationField()
    impact = models.CharField(max_length=6, choices=IMPACT_CHOICES)

    def __str__(self):
        return f"{self.sn} - {self.system_channel_name}"

class Serveraccess(models.Model):
    SERVER_CHOICES = [
        ('Fonepay', 'Fonepay'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
        ('SMS', 'SMS'),
        ('Mobile', 'Mobile'),
        ('Internet', 'Internet'),
    ]

    sn = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)
    server_name = models.CharField(max_length=50, choices=SERVER_CHOICES)
    purpose = models.TextField()
    access_by = models.CharField(max_length=255)
    provided_by = models.CharField(max_length=255)
    time = models.DurationField()

    def __str__(self):
        return f"{self.sn} - {self.server_name}"
