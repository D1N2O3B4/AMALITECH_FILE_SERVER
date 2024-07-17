from django import forms

class EmailForm(forms.Form):
    recipient_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)