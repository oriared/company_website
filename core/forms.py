from django.forms import ModelForm
from core.models import PriceImport


class PriceImportForm(ModelForm):
    class Meta:
        model = PriceImport
        fields = ('csv_file',)
