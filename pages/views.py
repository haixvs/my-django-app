from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to My First Django Website')

def about(request):
    return HttpResponse('<h1>About Us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')
