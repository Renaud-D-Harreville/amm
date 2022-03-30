from django import forms


class QCMForm(forms.Form):
    answers = forms.ChoiceField(widget=forms.RadioSelect)
    question = forms.JSONField(widget=forms.HiddenInput)


