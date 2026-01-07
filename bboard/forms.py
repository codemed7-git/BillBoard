from django import forms
from .models import Bb

class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'rubric']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Подробно опишите товар или услугу'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01'
            }),
            'rubric': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'Название товара',
            'content': 'Описание',
            'price': 'Цена',
            'rubric': 'Рубрика',
        }