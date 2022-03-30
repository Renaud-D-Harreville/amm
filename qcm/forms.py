from django import forms


class QCMForm(forms.Form):
    answers = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    question = forms.JSONField(widget=forms.HiddenInput)
