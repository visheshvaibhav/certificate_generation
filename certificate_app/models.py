
from django.db import models
from datetime import date


class Certificate(models.Model):
    recipient_name = models.CharField(max_length=255)
    certificate_id = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    # Allow manual setting of issue date
    issue_date = models.DateField(default=date.today)

    class Meta:
        permissions = [
            # Permission for generating certificate
            ('can_generate_certificate', 'Can generate certificate'),
            # Permission for viewing generated certificate
            ('can_view_generated_certificate', 'Can view generated certificate'),
        ]

    def __str__(self):
        return f'{self.recipient_name} - Certificate ID: {self.certificate_id}'
