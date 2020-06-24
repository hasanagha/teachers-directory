from django import forms
from account.models import Teacher


class ImportForm(forms.Form):
    file = forms.FileField()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('__all__')

    def clean(self):
        cleaned_data = self.cleaned_data
        subjects = cleaned_data['subjects']

        if subjects.count() > 5:
            raise forms.ValidationError("A teacher can have max 5 subjects.")

        return cleaned_data
