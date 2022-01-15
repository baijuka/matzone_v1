from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email',
                  'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Full Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'message': 'Message',
        }

        # self.fields['first_name'].widget.attrs['autofocus'] = True
        # for field in self.fields:
        #     placeholder = placeholders[field]
        #     self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = 'space-form rounded-0'
        #     self.fields[field].label = False