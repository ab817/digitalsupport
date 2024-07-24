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

class TechnicalSupportLog(models.Model):
    STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Processing', 'Processing'),
        ('Solved', 'Solved'),
    ]

    CATEGORY_CHOICES = [
        ('Mobile Banking', 'Mobile Banking'),
        ('Internet Banking', 'Internet Banking'),
        ('Esewa', 'Esewa'),
        ('Fonepay', 'Fonepay'),
        ('Khalti', 'Khalti'),
        ('NPS', 'NPS'),
        ('SMS', 'SMS'),
    ]

    REQUESTED_BY_CHOICES = [
        ('Branch', 'Branch'),
        ('COD', 'COD'),
        ('Customer', 'Customer'),
        ('Others', 'Others'),
        ('DBD', 'DBD'),
    ]

    ISSUE_LOGGED_TO_CHOICES = [
        ('F1soft', 'F1soft'),
        ('Fonepay', 'Fonepay'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
        ('NPS', 'NPS'),
        ('Others', 'Others'),
    ]

    sn = models.AutoField(primary_key=True)
    issue_no = models.CharField(max_length=20)
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    requested_by = models.CharField(max_length=20, choices=REQUESTED_BY_CHOICES)
    issue_logged_to = models.CharField(max_length=20, choices=ISSUE_LOGGED_TO_CHOICES)
    issue_description = models.TextField()
    reference_code = models.CharField(max_length=50)
    handling_person = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.issue_no
