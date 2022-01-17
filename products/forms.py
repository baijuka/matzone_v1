from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductVariation, Review


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        required=True, queryset=Category.objects.all())
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductVariationForm(forms.ModelForm):
    class Meta:
        model = ProductVariation
        fields = ('size', 'price', 'stock')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'review', 'rating']
