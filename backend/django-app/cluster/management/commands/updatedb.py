from django.core.management.base import BaseCommand
from cluster.rankings import RankingsData

class Command(BaseCommand):
    help = "Updates the player data in the database. "

    def handle(self, *args, **options):
        RankingsData.update_player_data()
