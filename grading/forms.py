from django import forms
from .models import Candidate, Recruiter, Task


GRADES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class GradingForm(forms.Form):
    recruiter = forms.ModelChoiceField(queryset=Recruiter.objects.all())
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())
    task = forms.ModelChoiceField(queryset=Task.objects.all())
    grade = forms.ChoiceField(choices=GRADES)
