from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ProductForm, ProductCategoryForm
from .models import Product, ProductCategory


class ProductList(ListView):
    model = Product
    extra_context = {'title': 'Список товаров'}


class ProductCreate(CreateView):
    model = Product
    template_name = 'goods/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('goods:product_list')
    extra_context = {'title': 'Добавление товара'}


class ProductsCategoryList(ListView):
    model = Product
    extra_context = {'title': 'Товары категории'}

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('pk', None) is not None:
            queryset = queryset.filter(categories__in=[self.kwargs.get('pk', None)])
        return queryset


class CategoryList(ListView):
    model = ProductCategory
    template_name = 'goods/category_list.html'
    extra_context = {'title': 'Список категорий'}


class CategoryCreate(CreateView):
    model = ProductCategory
    template_name = 'goods/product_create.html'
    form_class = ProductCategoryForm
    success_url = reverse_lazy('goods:category_list')
    extra_context = {'title': 'Добавление категории'}
