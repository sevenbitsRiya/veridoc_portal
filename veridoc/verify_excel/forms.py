from django import forms

from .models import VDG_M_ExcelDetails

class VDG_M_excelDetailsForm(forms.ModelForm):

    class Meta:
        model = VDG_M_ExcelDetails
        fields = ('Filepath',)
