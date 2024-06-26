from django import forms
from Musician_Pedia.models import Writer, Book

#Forms

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }

class InduvidualsBookForm(forms.ModelForm):
    
        class Meta:
             model = Book
             fields = ['book_title','release_date','book_ratings']
             widgets = {
                 'release_date': forms.DateInput(attrs={'type': 'date'})
             }