from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()

class ActForm(forms.Form):
    actDist = forms.DecimalField()
    actType = forms.CharField()
    actDuration = forms.CharField()
    actStartDate = forms.CharField()
    actAvgSpd = forms.DecimalField()
    actCalBurn = forms.IntegerField()
