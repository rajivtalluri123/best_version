from django import forms

class MomentsForm(forms.Form):
    proud_moments = forms.CharField(label='Enter ur proud moments that contributed towards ur goals this last 10 days', max_length=2000, widget=forms.Textarea(attrs={'cols':80, 'rows':6}))
    best_moments = forms.CharField(label='Enter ur best moments from the last 10 days which may or may not related to ur goal', max_length=2000, widget=forms.Textarea(attrs={'cols':80, 'rows':6}))

class TempSaveForm(forms.Form):
    temp_moments = forms.CharField(label="DON'T wanna miss this memory of today-- add it here for now", max_length=2000, widget=forms.Textarea(attrs={'cols':80, 'rows':6}))