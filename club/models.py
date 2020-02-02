from django.db import models
from django.conf import settings
from api_v0.models import BaseModel


class DartClub(BaseModel):
    CLUB_TYPE = (
        ('REGI', 'Registered Association'),
        ('CASU', 'Casual'),
        ('CACO', 'Casual Competitive'),
        ('OTHE', 'Other'),
    )

    MEET_FREQUENCY = (
        ('MONT', 'Monthly'),
        ('FORT', 'Fortnightly'),
        ('WEEK', 'Weekly'),
        ('OTHE', 'Other'),
    )
    club_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    date_established = models.DateField(
        blank=True,
        null=True,
    )

    club_status = models.CharField(
        choices=CLUB_TYPE,
        max_length=22,
        blank=False,
        null=False,
    )

    club_member_fees = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0.00,
        blank=True,
        null=True,
    )

    club_meeting_frequency = models.CharField(
        choices=MEET_FREQUENCY,
        max_length=22,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.club_name