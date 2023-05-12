from django import forms

from core.models import ProductPackaging


class PackageModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'Вес: {obj.weight} г., в коробке {obj.packaging} шт. Общий вес {obj.get_package_weight()} г.'


def build_add_form(*args, product):
    queryset = ProductPackaging.objects.filter(product=product)

    class CartAddProductForm(forms.Form):
        sku = PackageModelChoiceField(label='Фасовка:',
                                      queryset=queryset,
                                      to_field_name="sku",
                                      widget=forms.RadioSelect)
        quantity = forms.IntegerField(label='Количество', min_value=1, 
                                      max_value=999)
        override = forms.BooleanField(required=False, initial=False,
                                      widget=forms.HiddenInput)

    return CartAddProductForm(*args)
