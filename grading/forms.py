from django import forms
from .models import Candidate, Recruiter, Task


GRADES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        try:
            obj.first_name
            return obj.first_name + ' ' + obj.last_name

        except:
            return obj.title


class GradingForm(forms.Form):
    recruiter = MyModelChoiceField(queryset=Recruiter.objects.all())
    candidate = MyModelChoiceField(queryset=Candidate.objects.all())
    task = MyModelChoiceField(queryset=Task.objects.all())
    grade = forms.ChoiceField(choices=GRADES)
