from django import forms

from .models import User

class CreateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password',)


class InsertGEO(forms.Form):

    GEOID = forms.IntegerField(label = 'geoid');
    Block = forms.CharField(label = 'blockname');
    Population = forms.IntegerField(label = 'Population');
