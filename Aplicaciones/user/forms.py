from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# creacion de campos al momento de crear un nuevo perfil
# estos campos son para la creacion desde la pagina publica de los usuarios (falta guardar los extras)
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
    # se agrega este campo para poder verificar y crear el perfil del usuario relacionado
    is_internal = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)
# se envian los campos agregados para que aparezcan en el formulario del sistema y que cuando se llame al formulario desde login.html 
# se cree el registro llenando todos los campos
    class Meta: 
        model = User
        fields = ['username','email','password1','password2','pdi','name1','name2','lastname1','lastname2','brithday','phone','municipio','direccion','gender','is_internal']