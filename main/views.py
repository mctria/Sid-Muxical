from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout,login
from .form import *
from .models import Home, Latest_Episode, donation
from django.core.paginator import Paginator

# create your view here

# Global Latest episode fn
def Latest_ep(request):
    data = Latest_Episode.objects.all()

    return {'Latest_ep':data}

# global donation fn
def donation_data(request):
    data = donation.objects.all()

    return {"donation":data}

#global payment fn
def payment_fn(request):
    data = payment.objects.all()

    return {"payment":data}


#local fns
def home(request):
    data = Home.objects.all()
    title = Home_Edit.objects.all()
    length = len(data)

    context = {
        'data':data[:length-4],
        "title":title
    }

    return render(request,'main/home.html',context)
    
def podcasts(request,id,name):
    data = Home.objects.all()
    data1 = Home.objects.filter(id=id)
    id = id
    length = len(data)

    #pagination

    # p = Paginator(data, 4)  # creating a paginator object
    # getting the desired page number from url
    # if request.GET['page']:
    #     page_number = request.GET['page']
    # else:
    #     page_number = 1
    
    # if page_number:
    #     page_obj = p.get_page(page_number)  # returns the desired page object
    # elif page_number == None:
    #     # if page is empty then return last page
    #     page_obj = p.page(p.num_pages)
    # else:
    #     # if page_number is not an integer then assign the first page
    #     page_obj = p.page(1)

    context = {
        'data':data1,
        'data1':data[length-4:],
        "id":id,
        # 'data1': page_obj,
        }

    return render(request,'main/podcasts.html',context)

# Login Logout

def signin(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')


    return render(request,'CURD/add.html')

def signout(request):
    logout(request)
    return redirect('home')


# About

def privacy(request):

    return render(request,'main/privacy.html')

def terms(request):

    return render(request,'main/terms.html')

def about(request):

    if request.method == 'POST':
        email = request.POST['EMAIL']



    context = {}

    return render(request,'main/about-us.html',context)

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['message']

        


    context={}

    return render(request,'main/contact.html',context)