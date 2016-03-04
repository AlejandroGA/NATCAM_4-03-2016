#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import GatosSucursal

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class GatosSucursalForm(forms.ModelForm):
    class Meta:
        model = GatosSucursal
        fields = ('renta', 'luz', 'agua','telefono' ,'varios')






