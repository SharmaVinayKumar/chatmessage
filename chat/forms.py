from django import forms
from chat.models import Message


class ChatForm(forms.ModelForm):
    """
    Display form for Add or update information
    """
    class Meta:
        model = Message
        fields = ('body',)


class LoginForm(forms.Form):
    """
    Login Form
    """
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        if user_name:
            return user_name
        raise forms.ValidationError(_('Invalid Credential'))

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            return password
        else:
            raise forms.ValidationError(_('Invalid Credential'))
