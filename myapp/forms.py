from django import forms

class ContactForm(forms.Form):
    link = forms.CharField()
    keyword = forms.CharField()