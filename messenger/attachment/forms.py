from django import forms
# from attachment.models import Attachment

# class AttachmentForm(forms.ModelForm):
#     class Meta:
#         model = Attachment
#         fields = ['chat', 'user', 'message', 'type_attachment', 'url']

class AttachmentForm(forms.Form):
    # is_group_chat = forms.BooleanField(required=False)
    # topic = forms.CharField(max_length=32)
    # username = forms.CharField(max_length=16)
    chat_id = forms.CharField()
    user_id = forms.CharField()
    message_id = forms.CharField()
    type_attachment = forms.CharField()
    url = forms.CharField()
    media = forms.FileField(required=False)
    