from django import forms

class SignIn_User(forms.Form): # inicio sesion
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'campo',
        'placeholder': 'Username'
    }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 
        'class': 'campo',
    }), required=True)

class SignUp_User(forms.Form): # registro
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'campo',
        'placeholder': 'Username'
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'campo',
        'placeholder': 'Email'
    }), required=True)
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password', 
        'class': 'campo',
    }), required=True)
    
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password', 
        'class': 'campo',
    }), required=True)