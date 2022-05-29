from goods.models import ProductCategory
from visits.models import SiteVisit


def product_categories(request):
    return {'product_categories': ProductCategory.objects.all()}


def site_visits(request):
    return {'site_visits': SiteVisit.objects.count()}
