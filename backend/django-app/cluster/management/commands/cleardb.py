from django.core.management.base import BaseCommand
from cluster.models import Player

class Command(BaseCommand):
    help = "Updates the player data in the database. "

    def handle(self, *args, **options):
        Player.objects.all().delete()
