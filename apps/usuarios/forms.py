from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'
    

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields=[
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
                'username': 'Nommbre de Usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'email': 'Correo',

        }
        
