# Generated by Django 5.0.4 on 2024-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Downtime',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('system_channel_name', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('downtime_total_time', models.DurationField()),
                ('impact', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=6)),
            ],
        ),
    ]