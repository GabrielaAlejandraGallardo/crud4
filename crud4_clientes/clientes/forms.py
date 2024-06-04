from socket import fromshare
from django import forms 
from .models import Cliente

class ClientesForm(forms.ModelForm):
    class Meta:
        model=Cliente
        #fields='__all__'
        fields=('nom','ap','am','lenguaje','so','foto')
        labels ={
            'nom': 'Dame tu nombre:',
            'ap': 'Dame tu Apellido:'
        }
        
    
    def __init__(self, *args, **kwargs):
        super(ClientesForm,self).__init__(*args,**kwargs)
        self.fields['lenguaje'].empty_label="Selecciona"
        self.fields['so'].empty_label="Selecciona"
        self.fields['ap'].required=True
        self.fields['am'].required=False
        
        
       