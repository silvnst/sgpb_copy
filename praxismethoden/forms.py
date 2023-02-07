from .models import Method, File
from django import forms


class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = '__all__'
        exclude = ['likes']
        # widgets = {             'file_raw': forms.FileInput(attrs={'multiple': True}),         }

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'