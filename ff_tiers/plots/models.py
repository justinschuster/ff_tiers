import datetime

from os import path
from django.db import models
from django.utils import timezone

def plots_path():
    return os.path.join(setting.LOCAL_FILE_DIR, 'plots')

class Plots(models.Model):
    # Scoring format Constants
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

    plot_path = models.FilePathField(path=plots_path)
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
        return self.plot_path

    def was_created_today(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
