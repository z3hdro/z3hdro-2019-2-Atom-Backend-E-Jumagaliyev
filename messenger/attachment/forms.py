from django import forms
from attachment.models import Attachment

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['chat', 'user', 'message', 'type_attachment', 'url']
