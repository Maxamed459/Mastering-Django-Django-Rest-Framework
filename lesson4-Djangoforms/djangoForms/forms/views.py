from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.
def home_view(request):
    return render(request, 'forms/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.sendEmail()
            return redirect('success')
    else:
        form = ContactForm()
        context = {'form': form}
    return render(request, 'forms/contact.html', context)


def success_view(request):
    return render(request, 'forms/success.html')