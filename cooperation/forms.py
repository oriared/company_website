from django import forms
from cooperation.models import Cooperation


class CooperationForm(forms.ModelForm):
    class Meta:
        model = Cooperation
        fields = ('company', 'person', 'phone', 'email', 'city', 'text', 'file')
