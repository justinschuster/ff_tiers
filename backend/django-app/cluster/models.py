""" Models for cluster django app. """
from django.db import models

class Player(models.Model):
    """ Model to hold player ranking data. """
    ScoringType = models.TextChoices('ScoringType', 'STD PPR HPPR')
    PositionType = models.TextChoices('PositionType', 'QB RB WR TE K')
    scoring = models.TextField(choices=ScoringType.choices, null=True)
    consensus_ranking = models.IntegerField()
    player_name = models.TextField(unique=True)
    team_name_abbrev = models.CharField(max_length=10)
    position = models.TextField(choices=PositionType.choices)
    best_ranking = models.IntegerField()
    worst_ranking = models.IntegerField()
    average_ranking = models.IntegerField()
    ranking_std = models.IntegerField()

    def __str__(self):
        """ Returns player_name. """
        return self.player_name
