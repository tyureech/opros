from django import forms
from .models import MatterModel, OprosModel


class MatterChoicesForm(forms.Form):
    Варианты = forms.MultipleChoiceField()


class MatterForm(forms.ModelForm):
    number_matter = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = MatterModel
        fields = [
            'type_matter',
            'text_matter',
            'option_answer1',
            'option_answer2',
            'option_answer3',
            'option_answer4',
            'number_matter',
            ]


class OprosForm(forms.ModelForm):
    class Meta:
        model = OprosModel
        fields = [
            'id',
            'name',
            'description',
        ]
