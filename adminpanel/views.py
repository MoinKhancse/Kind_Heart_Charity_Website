
import os
from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User,slider
from django.contrib.auth import login,logout,authenticate
from django.conf import settings

def index(request):
    if request.user.is_authenticated:
        return render(request,'adminpanel/index.html')
    else:
        return redirect('login_page')


def reg_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            return redirect('reg_page')
        else:
            user_reg = User.objects.create_user(user_name,email,password_1)
            return redirect('login_page')
    return render(request, 'adminpanel/reg.html')

def login_page(request):
    if request.method == 'POST':
        a =request.POST.get('name')
        b =request.POST.get('password')
        user =authenticate(username=a, password=b)
        if user != None:
            login(request,user)
            return redirect('admin')
        else:
            return redirect('reg_page')
    return render(request, 'adminpanel/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def create_slider(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            slider_title = request.POST.get('slider_title')
            slider_desc = request.POST.get('slider_desc')
            slider_img = request.FILES['slider_image']
            
            slider_save = slider(
                slider_title = slider_title,
                slider_description = slider_desc,
                slider_image = slider_img,

            )
            slider_save.save()
        slider_all = slider.objects.all()
        return render(request, 'adminpanel/slider/add_slider.html',{'slider_all':slider_all})
    else:
        return redirect('login_page')


def edit(request,id):
   if request.user.is_authenticated:
        edite=slider.objects.get(id=id)
        
        if request.method == 'POST' and request.FILES:
            slider_title = request.POST.get('slider_title')
            slider_description = request.POST.get('slider_desc')

            if len(request.FILES) !=0:
                if len(edite.slider_image)>0:
                    os.remove(edite.slider_image.path)
                slider_image=request.FILES['slider_image']
            
            edit_save = slider(
                id=id,
                slider_title = slider_title,
                slider_description = slider_description,
                slider_image = slider_image,
            )
            edit_save.save()
            return redirect('add_slider')
        
        return render(request, 'adminpanel/slider/edit_slider.html',{'edit_all': edite })

def delete(request,id):
    delete_data=slider.objects.get(id=id)
    os.remove(delete_data.slider_image.path)
    delete_data.delete()
    return redirect('add_slider')