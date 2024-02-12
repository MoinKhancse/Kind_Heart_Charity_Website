from django.shortcuts import render,redirect
from adminpanel.models import slider
from website.models import Contact_form

def index(request):
    slider_info = slider.objects.all()
    
    if request.method == "POST":
        fname=request.POST.get('first-name')
        lname=request.POST.get('last-name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        cont=Contact_form(fname=fname,lname=lname,email=email,message=message)
        cont.save()

    context = {
        'slider':slider_info
    }
    return render(request,'website/index.html',context)

    