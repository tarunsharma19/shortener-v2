from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .short import Shortener

# Create your views here.
def contact(request):
    temp = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            link = form.cleaned_data['link']
            keyword = form.cleaned_data['keyword']
            temp = Shortener(link,keyword)
            print(temp)
    form = ContactForm()
    if (temp):
        return HttpResponse('https://shortener.tarundev.com/'+ keyword)
    return render(request , 'form.html', {'form':form})

