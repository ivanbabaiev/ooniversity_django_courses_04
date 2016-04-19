# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    """
    Input variables of the quadratic equation
    """
    a = forms.FloatField(label="коэффициент a", widget=forms.TextInput(attrs={'size': '10'}))
    b = forms.FloatField(label="коэффициент b", widget=forms.TextInput(attrs={'size': '10'}))
    c = forms.FloatField(label="коэффициент c", widget=forms.TextInput(attrs={'size': '10'}))

    def clean_a(self):
        if int(self.cleaned_data["a"]) == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        else:
            return self.cleaned_data["a"]
