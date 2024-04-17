from django import forms


class New_Slide_Form(forms.Form):  # inicio sesion
    title = forms.CharField(widget=forms.TextInput(), required=True)
    content = forms.CharField(widget=forms.Textarea(), required=True)

class Edit_Slide_Form(forms.Form):  # inicio sesion
    title = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'title'
    }), required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'content'
    }), required=True)    

class Search_User_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }), required=True)