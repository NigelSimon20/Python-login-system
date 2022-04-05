from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import signup, signin

class signUpForm(ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        
class signInForm(ModelForm):
    class Meta:
        model = signin
        fields = '__all__'