#-*- coding: utf-8 -*-

from django import forms

class Regbaseform(forms.Form):
    First_Name = forms.CharField(widget=forms.CharField())
    Last_Name = forms.CharField(widget=forms.CharField())
    Mobile_Number =  forms.IntegerField(widget=forms.IntegerField())
    Email = forms.CharField(widget=forms.CharField())


