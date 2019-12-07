from django import forms
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'chat']
