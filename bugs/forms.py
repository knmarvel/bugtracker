from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150
    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class AddCustomUser(forms.Form):
    username = forms.CharField(
        max_length=150
        )
    password = forms.CharField(
        widget=forms.PasswordInput()
        )
    display_name = forms.CharField(
        max_length=150
        )
    first_name = forms.CharField(
        max_length=30
        )
    last_name = forms.CharField(
        max_length=150
        )
    email = forms.EmailField()
