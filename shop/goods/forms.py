from django import forms

from .models import Product, ProductCategory


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'delivery_date',
            'price',
            'units',
            'provider',
            'categories',
        )
        widgets = {
            'delivery_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['categories'].queryset = ProductCategory.objects.all()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = (
            'name',
        )
