from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=999)
    override = forms.BooleanField(required=False, initial=False,
                                  widget=forms.HiddenInput)
