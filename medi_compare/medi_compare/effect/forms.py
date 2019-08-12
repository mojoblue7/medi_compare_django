from random import choices

from django import forms

from dal import autocomplete

from .models import Effect


class EffectRegisterForm(forms.Form):

    effect = forms.ModelMultipleChoiceField(
        queryset=Effect.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='effect-name-autocomplete'),
        error_messages={
            'required' : '효능을 입력해주세요.'
        }, 
        label = '효능', 
    )

    # POST된 데이터 값들 체크
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        effect_name = cleaned_data.get('effect')

        # print(cleaned_data)