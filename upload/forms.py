from django import forms
from index import models
from django.core.exceptions import ValidationError
from COMP3297_imageX.settings import GLOBAL_SETTINGS

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = [
            "title",
            "description",
            "tags",
            "category",
            "file"
        ]
    
    def clean(self):
        tags = self.cleaned_data.get('tags')
        if tags and len(tags) >  GLOBAL_SETTINGS['NO_OF_TAG']:
            raise ValidationError('Maximum '+str(GLOBAL_SETTINGS['NO_OF_TAG'])+' tags are allowed.')