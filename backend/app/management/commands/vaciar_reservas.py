from django.core.management.base import BaseCommand
from app.models import Box

class Command(BaseCommand):
    help = 'Vacía el campo reservas de todos los boxes'

    def handle(self, *args, **kwargs):
        boxes = Box.objects.all()
        for box in boxes:
            box.reservas = ''
            box.save()
        self.stdout.write(self.style.SUCCESS('Reservas vaciadas correctamente en todos los boxes.'))