import os
from django.conf import settings
from django.db import models

def plots_path():
	return os.path.join(setting.LOCAL_FILE_DIR, 'plots')

class Plots(models.Model):
	# Scoring format constants
	STANDARD = 'STND'
	PPR = 'FPPR'
	HALF_PPR = 'HPPR' # Don't know if I should make it an underscore or dash
	SCORING_FORMAT_CHOICES = (
		(STANDARD, 'standard'),
		(PPR, 'ppr'),
		(HALF_PPR, 'half_ppr'),
	)

	# Position constants
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
	creation_date = models.DateTimeField('creation date')
	scoring_format = models.CharField(
		max_length=4,
		choices=SCORING_FORMAT_CHOICES,
		default=STANDARD,
	)	
	positon = models.CharField(
		max_length=2,
		choices=POSITION_CHOICES,
		default=QB,
	)
