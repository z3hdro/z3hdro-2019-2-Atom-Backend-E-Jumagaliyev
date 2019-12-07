from django import forms

class MessageForm(forms.Form):
    chat_id = forms.CharField()
    content = forms.CharField(required=False)
    attachment_type = forms.CharField()
    geolocation_url = forms.CharField(required=False)
    media = forms.FileField(required=False)
