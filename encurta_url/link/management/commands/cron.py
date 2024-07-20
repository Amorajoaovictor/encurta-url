from django.utils import timezone
from django.core.management.base import BaseCommand
from link.models import Link

class Command(BaseCommand):
    help = 'Description of your command'

    def handle(self, *args, **kwargs):
        deletados = Link.objects.filter(valid_until__lt=timezone.now()).delete()
        for deletado in deletados:
            print(f"Deletado {deletado} links")