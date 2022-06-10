import random

from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from goods.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Creates n number of products'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        categories = [cat for cat in ProductCategory.objects.all()]
        for i in range(options['amount']):
            name = f'Product {i}'
            if not Product.objects.filter(name=name).exists():
                product = mixer.blend(Product, name=name)
                max_cat_id = random.randint(0, len(categories))
                for j in range(random.randint(0, max_cat_id), max_cat_id):
                    product.categories.add(categories[j])
                product.save()
