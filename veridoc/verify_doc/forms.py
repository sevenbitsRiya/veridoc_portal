from django import forms

from .models import VDG_M_documentDetails

class VDG_M_documentDetailsForm(forms.ModelForm):

    class Meta:
        model = VDG_M_documentDetails
        fields = ('Fileurl',)
