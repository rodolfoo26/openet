from django.contrib.auth import forms
from django import forms as forms_1
from .models import User

CURSOS = (
    (u'TDS', u'TDS'),
    (u'TGI', u'TGI'),
    (u'DIREITO', u'DIREITO'),
    (u'CONTABEIS', u'CONTABEIS'),
)



class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):

    email = forms_1.EmailField(max_length=100)
    curso = forms_1.CharField(widget=forms_1.RadioSelect(choices=CURSOS))

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2','ano','matricula','curso']
