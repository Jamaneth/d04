from django.shortcuts import render
from ex02.forms import ContactForm

# Create your views here.
def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():

        email = form.cleaned_data['email']
        form_sent = True
        form.save()

    return render(request, 'ex02/contact.html', locals())
