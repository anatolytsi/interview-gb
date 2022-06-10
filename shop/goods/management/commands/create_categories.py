from django.core.management.base import BaseCommand
from goods.models import ProductCategory


class Command(BaseCommand):
    help = 'Creates n number of categories'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        for i in range(options['amount']):
            name = f'Category {i}'
            if not ProductCategory.objects.filter(name=name).exists():
                category = ProductCategory.objects.create(name=name)
                category.save()
