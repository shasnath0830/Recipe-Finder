from django.core.management.base import BaseCommand
from api.models import Recipe

class Command(BaseCommand):
    help = 'Delete all existing recipes'

    def handle(self, *args, **kwargs):
        Recipe.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all existing recipes'))
