from django import forms
from django.contrib.auth.models import User

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['username'].widgets.attrs['placeholder'] = 'Your username'
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    # Trechos comentados para evitar conflitos com solução na parte anterior do código. Mas abaixo segue sendo possibilidade.
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            #'placeholder': 'Your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        label='Password'
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            #'placeholder': 'Repeat your password'
        }),
        label='Password2'
    )
    
    # Trechos comentados para evitar conflitos com solução na parte anterior do código. Mas abaixo segue sendo possibilidade.
    class Meta:
        model = User
        #fields = '__all__' #__all__ trará todos os campos de User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
         # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'The e-mail must be valid.',
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                #'placeholder': 'Type your username here',
                'class': 'input text-input'
            }),
            'password': forms.PasswordInput(attrs={
                #'placeholder': 'Type your password here'
            })
        }


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = forms.ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise forms.ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })