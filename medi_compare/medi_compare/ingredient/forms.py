from django import forms

class IngredientRegisterForm(forms.Form):
        
    ingredient_name = forms.ChoiceField(
        error_messages={
            'required' : '성분명을 선택하거나 생성해주세요.'
        }, label = '성분명'
    )
    
    ingredient_class = forms.ChoiceField(
        error_messages={
            'required' : '성분 분류를 선택하거나 생성해주세요.'
        }, label = '성분 분류'
    )
    
    ingredient_volume = forms.IntegerField(
        error_messages={
            'required' : '성분함량을 입력해주세요.'
        }, label = '성분 함량'
    )
    
    ingredient_unit = forms.ChoiceField(
        error_messages={
            'required' : '단위명을 선택하거나 생성해주세요.'
        }, label = '단위명'
    )
    
    ingredient_detail_content = forms.CharField(
        required=False,
        initial='',    
        label='성분 상세 내용'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        ingredient_name = cleaned_data.get('ingredient_name')
        ingredient_class = cleaned_data.get('ingredient_class')
        ingredient_volume = cleaned_data.get('ingredient_volume')
        ingredient_unit = cleaned_data.get('ingredient_unit')
        ingredient_detail_content = cleaned_data.get('ingredient_detail_content')