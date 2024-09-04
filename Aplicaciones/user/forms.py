from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# creacion de campos al momento de crear un nuevo perfil

class CreateUserForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    email = forms.EmailField()
    pdi = forms.IntegerField()
    name1 = forms.CharField()
    name2 = forms.CharField()
    lastname1 = forms.CharField()
    lastname2 = forms.CharField()
    brithday = forms.DateField()
    phone = forms.IntegerField()
    municipio = forms.CharField()
    direccion = forms.CharField()
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        label="Gender"
    )
    class Meta: 
        model = User
        fields = ['username','email','password1','password2','pdi','name1','name2','lastname1','lastname2','brithday','phone','municipio','direccion','gender']