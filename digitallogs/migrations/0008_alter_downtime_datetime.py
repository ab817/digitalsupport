# Generated by Django 5.0.4 on 2024-08-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitallogs', '0007_alter_serveraccess_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downtime',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
