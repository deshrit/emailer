from django import forms


class EmailerForm(forms.Form):
    receiver = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'someone@example.com'
            }
        ),
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email subject ..'
            }
        ),
        error_messages={
            'required': 'Subject field is required.',
        },
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email body ..'
            }
        ),
        error_messages={
            'required': 'Message field is required.'
        },
    )