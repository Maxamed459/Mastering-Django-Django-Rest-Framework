from django.forms import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def sendEmail(self):
        print(f'Sending Email from {self.cleaned_data['email']}, with message {self.cleaned_data['message']}')