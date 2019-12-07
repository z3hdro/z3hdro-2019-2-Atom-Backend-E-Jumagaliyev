from django import forms
# from chats.models import Chat

# class ChatForm(forms.ModelForm):
#     class Meta:
#         model = Chat
#         fields = ['is_group_chat', 'topic', 'last_message']

class ChatForm(forms.Form):
    is_group_chat = forms.BooleanField(required=False)
    topic = forms.CharField(max_length=32)
    username = forms.CharField(max_length=60)
    