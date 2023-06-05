from django import forms
from django.forms import ModelForm
from core.models import PriceImport


class PriceImportForm(ModelForm):
    change_packs = forms.BooleanField(label='Автоматически изменять доступность',
                                      required=False)

    class Meta:
        model = PriceImport
        fields = ('csv_file',)
