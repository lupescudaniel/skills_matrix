from django import forms


class SkillForm(forms.Form):
    skill = forms.CharField()
    proficiency = forms.CharField()
    years_experience = forms.IntegerField()
