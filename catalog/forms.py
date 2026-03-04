from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    # Список запрещенных слов
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Стилизация форм"""
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        """Валидация названия"""
        cleaned_data = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово: {word}')
        return cleaned_data

    def clean_description(self):
        """Валидация описания"""
        cleaned_data = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово: {word}')
        return cleaned_data

    def clean_price(self):
        """Валидация цены"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной') #
        return price