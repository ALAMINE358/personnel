from django import forms
from .models import *


        
class FormPersonnel(forms.ModelForm):
    
    class Meta:

        model = Personnel

        fields = '__all__'

    def __init__(self, *arg, **kwargs):
        super(FormPersonnel,self).__init__(*arg, **kwargs)
        self.fields['identifiant']=forms.CharField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'text',
                    'id' : 'identifiant',
            }))

        self.fields['prenom']=forms.CharField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'text',
                    'id' : 'prenom',
            }))
        self.fields['nom']=forms.CharField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'text',
                    'id' : 'nom',
            }))
        self.fields['fonction']=forms.CharField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'text',
                    'id' : 'fonction',
            }))
        self.fields['tel']=forms.IntegerField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'number',
                    'id' : 'tel',
            }))
        self.fields['email']=forms.CharField(widget=forms.TextInput(
            attrs={'class' :'form-control',
                    'type' : 'email',
                    'id' : 'email',
            }))
      