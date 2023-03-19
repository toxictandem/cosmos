from django import forms

class InputForm(forms.Form):
    forma = forms.CharField(label='Ввод')