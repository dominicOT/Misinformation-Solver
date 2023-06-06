from django.shortcuts import render
from .models import subscribe

# Create your views here.

def index(request):
    if request.method == 'POST':
        subMail = request.POST['subMail']

        submit_mail = subscribe(subMail=subMail)
        submit_mail.save()


    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def join(request):
    return render(request, 'join.html')

