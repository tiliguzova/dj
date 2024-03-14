from django import forms

from info.models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('name', 'text', 'rating', 'price')
