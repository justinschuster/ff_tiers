"""
Code for the cluster app Admin page.
"""

from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    """
    Changes admin view for the Player model.
    """
    list_display = (
        'player_name',
        'consensus_ranking',
        'position',
        'best_ranking',
        'worst_ranking',
        'average_ranking',
        'ranking_std'
    )

admin.site.register(Player, PlayerAdmin)
