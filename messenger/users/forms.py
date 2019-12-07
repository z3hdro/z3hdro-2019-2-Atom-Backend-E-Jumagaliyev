from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(required=False, max_length=25)
    last_name = forms.CharField(required=False, max_length=25)
    bio = forms.CharField(required=False, max_length=250)
    avatar = forms.FileField(required=False)
