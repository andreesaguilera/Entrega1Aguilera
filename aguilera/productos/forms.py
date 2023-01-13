from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea)
    stock = forms.IntegerField()