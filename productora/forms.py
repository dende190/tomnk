from django import forms

class Formularios(forms.Form):
	nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	email = forms.EmailField( widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	mensaje = forms.CharField(widget=forms.Textarea)