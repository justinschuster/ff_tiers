from django.db import models

class Player(models.Model):
    consensus_ranking = models.IntegerField()
    player_name = models.TextField()
    team_name_abbrev = models.CharField(max_length=10)
    position = models.CharField(max_length=3)
    bye_week = models.IntegerField()
    best_ranking = models.IntegerField()
    worst_ranking = models.IntegerField()
    average_ranking = models.IntegerField()
    ranking_std = models.IntegerField()
    average_draft_position = models.IntegerField()
    vs_average_draft_position = models.IntegerField()

    def __str__(self):
        return self.player_name

