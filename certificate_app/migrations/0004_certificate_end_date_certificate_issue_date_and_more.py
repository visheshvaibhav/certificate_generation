# Generated by Django 4.2.4 on 2024-08-08 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("certificate_app", "0003_certificate_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="end_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="certificate",
            name="issue_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="certificate",
            name="start_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
