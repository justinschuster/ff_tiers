import datetime

from django.utils import timezone
from django.conf import settings
from django.db import models

class Plot(models.Model):
    # Scoring Format Constants
    STANDARD = 'STND'
    PPR = 'FPPR'
    HALF_PPR = 'HPPR'
    SCORING_FORMAT_CHOICES = (
        (STANDARD, 'standard'),
        (PPR, 'ppr'),
        (HALF_PPR, 'half_ppr'),
    )

    # Position Constants
    QB = 'QB'
    RB = 'RB'
    WR = 'WR'
    TE = 'TE'
    K = 'K'
    POSITION_CHOICES = (
        (QB, 'QB'),
        (RB, 'RB'),
        (WR, 'WR'),
        (TE, 'TE'),
        (K, 'K'),
    )

    # Model Fields
    plot_name = models.TextField(default='test_field')
    creation_date = models.DateTimeField('creation_date')
    scoring_format = models.CharField(
        max_length=4,
        choices=SCORING_FORMAT_CHOICES,
        default=STANDARD,
    )
    position = models.CharField(
        max_length=4,
        choices=POSITION_CHOICES,
        default=QB,
    )

    def __str__(self):
        return self.plot_name

    def was_created_today(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

    def get_position(self):
        """ Returns the position of a plot. """
        return self.position
