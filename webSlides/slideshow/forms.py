from django import forms


class New_Slide_Form(forms.Form):  # inicio sesion
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Titulo'
    }), required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Contenido'
    }), required=True)