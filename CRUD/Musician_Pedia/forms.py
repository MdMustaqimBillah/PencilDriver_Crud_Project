from django import forms
from Musician_Pedia.models import Musician, Album

#Forms

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }