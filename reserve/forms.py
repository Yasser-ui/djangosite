from django import forms

from .models import Reserve

class ReserveForm(forms.ModelForm):

    class Meta:
        model = Reserve
        fields = ('firstName', 'lastName', 'email', 'phone', 'resaDate', 'guestNumbr', 'trimeFrom', 'timeTo', 'comment')
