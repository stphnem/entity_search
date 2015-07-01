from django import forms

class InputForm(forms.Form):
    textInput = forms.CharField(widget=forms.Textarea, required=False)


