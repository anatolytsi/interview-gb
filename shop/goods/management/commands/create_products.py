from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from goods.models import Product


class Command(BaseCommand):
    help = 'Creates n number of products'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        for i in range(options['amount']):
            name = f'Product {i}'
            if not Product.objects.filter(name=name).exists():
                product = mixer.blend(Product, name=name)
                product.save()
