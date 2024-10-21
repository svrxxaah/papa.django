from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def faq(request):
    return render(request, 'app2/faq.html')

def contact(request):
    return render(request, 'app2/contact.html')
