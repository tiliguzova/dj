from django import forms

from info.models import Info


class InfoForm(forms.ModelFrom):
    class Meta:
        model = Info
        fields = ('name', 'text', 'rating', 'price')
