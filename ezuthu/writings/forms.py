from django import forms
from .models import Writing, Writer

class WritingSubmissionForm(forms.Form):
    writer_name = forms.CharField(
        max_length=100,
        label="എഴുത്തുകാരന്റെ പേര്"
    )
    title = forms.CharField(
        max_length=200,
        label="എഴുത്തിന്റെ പേര്"
    )
    content = forms.CharField(
        widget=forms.Textarea,
        label="എഴുത്ത്"
    )
