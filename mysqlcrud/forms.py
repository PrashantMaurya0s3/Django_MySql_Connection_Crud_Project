from django import forms
from mysqlcrud.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'uemail': forms.TextInput(attrs={'class': 'form-control'}),
            'upassword': forms.TextInput(attrs={'class': 'form-control'}),

        }