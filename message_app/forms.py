from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Browse',
        help_text='max. 42 megabytes'
    )
