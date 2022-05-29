from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ProductForm
from .models import Product


class ProductList(ListView):
    model = Product
    extra_context = {'title': 'Список товаров'}


class ProductCreate(CreateView):
    model = Product
    template_name = 'goods/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('goods:product_list')
    extra_context = {'title': 'Добавление товара'}
