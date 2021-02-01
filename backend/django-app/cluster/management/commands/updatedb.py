from django.core.management.base import BaseCommand
from cluster.rankings import Rankings

class Command(BaseCommand):
    help = "Updates the player data in the database. "

    def handle(self, *args, **options):
        Rankings.update_player_data()
