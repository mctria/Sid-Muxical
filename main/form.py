from .models import *
from django import forms


class main_form(forms.Form):
    class Meta:
        model = Home
        fields = "__all__"