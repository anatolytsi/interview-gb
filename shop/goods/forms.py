from django import forms

from .models import Product


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
        )
        widgets = {
            'delivery_date': DateInput()
        }
