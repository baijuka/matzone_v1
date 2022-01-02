from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductVariation, Review


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(required=True, queryset=Category.objects.all())
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # self.fields['category'].choices = friendly_names
        # self.fields['category'].choices = Category.objects.all().values_list('id', 'name')
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductVariationForm(forms.ModelForm): 
    class Meta:
        model = ProductVariation
        fields = ('size', 'price', 'stock')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].choices = Category.objects.all().values_list('id', 'name')
    #     self.fields['product'].choices = Product.objects.all().values_list('id', 'name')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject','review', 'rating']

