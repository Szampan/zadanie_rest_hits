from django.core.management.base import BaseCommand
from rest_hits_app.models import Artist, Hit
import random

class Command(BaseCommand):
    help = 'Populates the database with sample artists and hits'

    def handle(self, *args, **options):
        artist_names = [
            ('John', 'Doe'), ('Jane', 'Smith'), ('Michael', 'Johnson')
        ]
        for first_name, last_name in artist_names:
            Artist.objects.create(first_name=first_name, last_name=last_name)
        
        for i in range(20):
            artist = random.choice(Artist.objects.all())
            Hit.objects.create(
                title=f'Hit {i+1}',
                artist=artist
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database')) 