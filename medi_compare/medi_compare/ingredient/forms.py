from random import choices

from django import forms

from dal import autocomplete

from .models import Ingredient_class, Ingredient_name, Ingredient_unit


class IngredientRegisterForm(forms.Form):

    ingredient_name = forms.ModelChoiceField(
        queryset=Ingredient_name.objects.all(),
        widget=autocomplete.ModelSelect2(url='ingredient-name-autocomplete'),
        error_messages={
            'required' : '성분명을 입력해주세요.'
        }, 
        label = '성분명', 
    )

    ingredient_class = forms.ModelChoiceField(
        queryset=Ingredient_class.objects.all(),
        widget=autocomplete.ModelSelect2(url='ingredient-class-autocomplete'),
        error_messages={
            'required' : '성분 분류를 입력해주세요.'
        }, label = '성분 분류'
    )
    
    ingredient_volume = forms.IntegerField(
        min_value=0,
        error_messages={
            'required' : '성분함량을 입력해주세요.',
            'min_value' : '0 이상의 값을 입력해주세요. '
        }, label = '성분 함량', 
    )

    ingredient_unit = forms.ModelChoiceField(
        queryset=Ingredient_unit.objects.all(),
        widget=autocomplete.ModelSelect2(url='ingredient-unit-autocomplete'),
        error_messages={
            'required' : '단위명을 선택해주세요.'
        }, 
        label = '단위명',
    )
    
    ingredient_detail_content = forms.CharField(
        required=False,
        initial='',    
        label='성분 상세 내용'
    )

    # POST된 데이터 값들 체크
    def clean(self):
        cleaned_data = super().clean()
        ingredient_name = cleaned_data.get('ingredient_name')
        ingredient_class = cleaned_data.get('ingredient_class')
        ingredient_volume = cleaned_data.get('ingredient_volume')
        ingredient_unit = cleaned_data.get('ingredient_unit')
        ingredient_detail_content = cleaned_data.get('ingredient_detail_content')

        print(cleaned_data)