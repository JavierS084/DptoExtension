from django import forms
from .models import Alumnos

class Alumnosform(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields = ['nombre', 'apellido', 'CI', 'email', 'telefono', 'sede_id', 'carrera_id', 'horaExtension', 'Documento']
        labels={
            'nombre':'Nombre del Alumno',
            'apellido':'Apellido del Alumno',
            'CI':'Cedula de Identidad',
            'email':'Correo',
            'telefono':'Telefono',
            'sede_id':'Sede',
            'carrera_id':'Carrera',
            'horaExtension':'Hora de Extension',
            'Documento':'Adjuntar Certificado'
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'nombre'
                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'apellido'
                }
            ),
            'CI':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'CI'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'id':'email'
                }
            ),
            'telefono':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'telefono'
                }
            ),
            'sede_id':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'sede_id'
                }
            ),
            'carrera_id':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'carrera_id'
                }
            ),
            'horaExtension':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'id':'horaExtension'
                }
            ),
            'Documento':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'id_Documento'
                }
            )

        }