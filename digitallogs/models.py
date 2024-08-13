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
    datetime = models.DateTimeField()
    system_channel_name = models.CharField(max_length=255)
    reason = models.TextField()
    downtime_total_time = models.DurationField()
    impact = models.CharField(max_length=6, choices=IMPACT_CHOICES)

    def __str__(self):
        return f"{self.sn} - {self.system_channel_name}"

class Serveraccess(models.Model):
    SERVER_CHOICES = [
        ('Fonepay (Live)', 'Fonepay (Live)'),
        ('Fonepay (Test)', 'Fonepay (Test)'),
        ('Esewa (Live)', 'Esewa (Live)'),
        ('Esewa (Test)', 'Esewa (Test)'),
        ('Khalti (Live)', 'Khalti (Live)'),
        ('Khalti (Test)', 'Khalti (Test)'),
        ('SMS', 'SMS'),
        ('Mobile (Live)', 'Mobile (Live)'),
        ('Mobile (Test)', 'Mobile (Test)'),
        ('Internet Banking (Live)', 'Internet Banking (Live'),
        ('Internet Banking (Test)', 'Internet Banking (Test'),
        ('Online Account(Test)', 'Online Account(Test)'),
        ('Online Account(Live)', 'Online Account(Live)'),
        ('Customer 360(Test)', 'Customer 360(Test)'),
        ('Kisan System(Live)', 'Kisan System(Live)'),
        ('IPS', 'IPS'),
        ('Connect IPS', 'Connect IPS'),
        ('Corporate Pay', 'Corporate Pay'),
        ('ECC', 'ECC'),
        ('Nepal Pay QR', 'Nepal Pay QR'),
        ('Gokyo', 'Gokyo'),
        ('Foneloan (Test)', 'Foneloan (Test)'),
        ('Foneloan (Live)', 'Foneloan (Live)'),
        ('Digital Chautari', 'Digital Chautari'),
    ]

    sn = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    server_name = models.CharField(max_length=50, choices=SERVER_CHOICES)
    purpose = models.TextField()
    access_by = models.CharField(max_length=255)
    provided_by = models.CharField(max_length=255)
    time = models.DurationField()

    def __str__(self):
        return f"{self.sn} - {self.server_name}"

from django.db import models
from django.utils.timezone import now

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
        ('ATM', 'ATM'),
        ('Kisan', 'Kisan'),
        ('POS', 'POS'),
        ('Online Account', 'Online Account'),
        ('IPS', 'IPS'),
        ('ECC', 'ECC'),
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
        ('Peace Nepal', 'Peace Nepal'),
        ('Digihub', 'Digihub'),
        ('NCHL', 'NCHL'),
        ('Gokyo', 'Gokyo'),
        ('Others', 'Others'),
    ]

    HANDLING_CHOICES = [
        ('Ankit Bhattarai', 'Ankit Bhattarai'),
        ('Aakriti Silwal', 'Aakriti Silwal'),
        ('Bom Bahadur BK', 'Bom Bahadur BK'),
        ('Bikash Devkota', 'Bikash Devkota'),
        ('Birendra Yadav', 'Birendra Yadav'),
        ('Shreya Shrestha', 'Shreya Shrestha'),
        ('Prakriti Gyawali', 'Prakriti Gyawali'),
        ('Manju Upreti', 'Manju Upreti'),
        ('Arjun Poudel', 'Arjun Poudel'),
        ('Prakash Pandey', 'Prakash Pandey'),
        ('Priya Gupta', 'Priya Gupta'),
    ]

    sn = models.AutoField(primary_key=True)
    issue_no = models.CharField(max_length=20, unique=True, editable=False)
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    requested_by = models.CharField(max_length=20, choices=REQUESTED_BY_CHOICES)
    issue_logged_to = models.CharField(max_length=20, choices=ISSUE_LOGGED_TO_CHOICES)
    issue_description = models.TextField()
    reference_code = models.CharField(max_length=50)
    handling_person = models.CharField(max_length=30, choices=HANDLING_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.issue_no

    def save(self, *args, **kwargs):
        if not self.issue_no:
            # Generate issue_no
            last_issue = TechnicalSupportLog.objects.order_by('-sn').first()
            if last_issue:
                try:
                    last_number = int(last_issue.issue_no.split('DBD - ')[-1])
                except ValueError:
                    last_number = 0
                new_number = last_number + 1
            else:
                new_number = 1
            self.issue_no = f'DBD - {new_number:02d}'
        super().save(*args, **kwargs)


class TaskLog(models.Model):
    TASK_TYPE_CHOICES = [
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
        ('Improvement', 'Improvement'),
        ('Software', 'Software')
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('Overall', 'Overall'),
        ('Board 1', 'Board 1'),
        ('Board 2', 'Board 2'),
    ]

    id = models.AutoField(primary_key=True)
    task_details = models.TextField()
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES)
    assigned_date = models.DateField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    assigned_to = models.CharField(max_length=100)
    days_allocated = models.IntegerField()
    solved_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.task_type} - {self.task_details[:50]}'