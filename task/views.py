from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'task/home.html')

def about(request):
    return render(request, 'task/about.html')

def contact(request):
    return render(request, 'task/contact.html')