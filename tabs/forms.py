from django import forms

class EditCommentForm(forms.Form):
    comment = forms.CharField(label='Your name', max_length=100)