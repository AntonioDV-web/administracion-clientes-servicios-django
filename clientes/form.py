from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = ["nombre", "correo", "telefono", "fotografia", "activo"]

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe de tener al menos 2 caracteres")
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data["correo"].strip()
        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise forms.ValidationError("Ingrese un correo valido")
        return correo
