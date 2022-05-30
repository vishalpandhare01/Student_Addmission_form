import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import AddmisionForm
from django.core.mail import send_mail ,EmailMultiAlternatives

# Create your views here.
def reg(request):
    if request.method =="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.create_user(email=email,username=username,password=password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        name=first_name
        
        send_mail(
            'Register Successfully',
            'Thanks for reching our web site !',
            'bisalp0102@gmail.com',
            [ email ],
            fail_silently=False,
        )
        return render(request,"index.html",{'name':name})
        
    return render(request,"register.html")

# login
from django.contrib.auth import authenticate
def login1(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/main")
        else:
            return HttpResponse("login invalid...")
    return render(request,"login.html")        


#FORM    
def main(request):
        # create a form instance and populate it with data from the request:
    if request.method == 'POST':
        photo=request.POST.get("photo")
        full_name=request.POST.get("full_name")
        fathare_name=request.POST.get("fathare_name")
        Phone_Number=request.POST.get("Phone_Number")
        email=request.POST.get("email")
        adhar_number=request.POST.get("adhar_number")
        Address=request.POST.get("Address")
        date=request.POST.get("date")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        form=AddmisionForm(photo=photo,full_name=full_name,fathare_name=fathare_name,Phone_Number=Phone_Number,adhar_number=adhar_number,Address=Address,date=date,age=age,gender=gender,email=email)
        form.save()
        subject = 'Admission form submitted Successfully'
        from_email ='bisalp0102@gmail.com'
        text_content = 'Thanks for reching our web site we will get back to soon  !'
        html_content = '<p>Thanks for reching our web site we will get back to soon  ! this is an <strong>important</strong> message. from US</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email,[ email ])
        msg.attach_alternative(html_content, "text/html")   
        msg.send()   

        obj = form.full_name
        return render( request,'saved.html',{'obj':obj})
    return render(request,"main.html")


# from django.core.mail import EmailMultiAlternatives




#log out
def logout1(request):
    logout(request)
    return redirect('/')      