from django import forms
from new_app.models import customer
class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ("__all__")

