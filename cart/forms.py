from django.core.exceptions import ValidationError
from django import forms
from django.forms import BaseFormSet


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='', min_value=0,
                                  max_value=999, required=False)
    product_sku = forms.CharField(widget=forms.HiddenInput)


class CartUpdateProductForm(forms.Form):
    quantity = forms.IntegerField(label='', min_value=1, max_value=999)


class BaseAddProductFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        if not any(map(lambda x: x.cleaned_data.get('quantity'), self.forms)):
            raise ValidationError('Не заполнена ни одна форма.')
