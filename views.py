from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from rs.settings import EMAIL_HOST_USER
from django.contrib import  messages
from django.core.mail import send_mail
from  django.conf import settings
from  django.contrib.auth import authenticate
import uuid
from  django.contrib.auth.models import User
from django.http import  HttpResponse
from .forms  import *
from  .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':

        email=request.POST.get('email')
        pas=request.POST.get('password')
        uname=request.POST.get('uname')

        if User.objects.filter(email=email).first():
            messages.success(request,"email already taken")
            return redirect(register)

        if User.objects.filter(username=uname).first():
            messages.success(request,"username already taken")
            return redirect(register)

        user_obj=User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_register(email,auth_token)

        return redirect(success)
    return render(request,'register.html')

def send_mail_register(email,token):
    subject="your account has been verified"
    message=f"pass the link to verify your account http:127.0.0.1:8000/verify/{token}"
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)
# def success(request):
#     return render(request,'success.html')

def success(request):
    return render(request,"success.html")

def login(request):
    global User;
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return  redirect(login)
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile verified cheek your email')
            return  redirect(login)
        User=authenticate(username=username,password=pas)

        if User is None:
            messages.success(request,'wrong password or username')
            return  redirect(login)
        # return  HttpResponse("success")
        obj=profile.objects.filter(user=user_obj)
        return render(request,'1.html',{'obj':obj})

    return  render(request,'login.html')

def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'ur account verified')
        return redirect(login)
    else:
        return redirect(error)

def error(request):
    return  render(request,'error.html')
def login2(request):
    if request.method == "POST":
        form = logform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['pas']
            users = regmodel.objects.all()

            for user in users:
                if email == user.email and password == user.password:
                    data=itemmodel.objects.all()
                    nm=[]
                    img=[]
                    ids=[]
                    for i in data:
                        a=i.name
                        nm.append(a)

                        path=i.image
                        img.append(str(path).split("/")[-1])
                        d=i.id
                        ids.append(d)

                        s=zip(nm,img,ids)
                    # j=review_model.objects.get(id=id)
                    return render(request, '2.html', {'s':s})

            return HttpResponse("Email and password incorrect....")

        return HttpResponse("Enter valid data...")

    return  render(request,'login2.html')
def register2(request):
    if request.method=="POST":
        a=regform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            eml=a.cleaned_data['email']
            ag=a.cleaned_data['age']
            co=a.cleaned_data['country']
            pas=a.cleaned_data['password']
            cpass=a.cleaned_data['cpassword']
            if pas==cpass:
                b=regmodel(name=nm,email=eml,password=pas,age=ag,country=co)
                b.save()
                # return  HttpResponse("successfully registered")
                return render(request,'ss.html')
            else:
                return HttpResponse("password and confirm password not match")
        else:
            return HttpResponse("enter valid data")
    return render(request,'register2.html')

def add(request, id):
    x = profile.objects.get(id=id)

    if request.method == "POST":
        a = itemform(request.POST, request.FILES)
        if a.is_valid():
            em= a.cleaned_data['email']
            nam = a.cleaned_data['name']
            ty =a.cleaned_data['type']
            ing = a.cleaned_data['ingree']
            s = a.cleaned_data['step']
            img = a.cleaned_data['image']
            b = itemmodel(email=em,name=nam,type=ty ,ingree=ing, step=s, image=img)
            b.save()
            return render(request, "s.html")
        else:
            # Display form errors
            return render(request, 'additem.html', {'form': a, 'x': x})

    a = itemform()
    return render(request, 'additem.html', {'form': a, 'x': x})
#
# def add(request,id):
#     if request.method == "POST":
#         a = itemform(request.POST, request.FILES)
#         if a.is_valid():
#             nam = a.cleaned_data['name']
#             ing = a.cleaned_data['ingree']
#             s = a.cleaned_data['step']
#             img = a.cleaned_data['image']
#             b = itemmodel(name=nam, ingree=ing, step=s, image=img)
#             b.save()
#             return render(request,"s.html")
#         else:
#             # Display form errors
#             # x= profile.objects.get(id=id)
#             return render(request, 'additem.html', {'form': a,'error_message': 'Form submission failed.'})
#     else:
#         a = itemform()
#         x= profile.objects.get(id=id)
#         return render(request, 'additem.html', {'form': a,'x ':x })

def view(request,id):
    y=profile.objects.get(id=id)
    y_email=y.user.email

    data=itemmodel.objects.all()
    nm=[]
    img=[]
    ids=[]

    for i in data:
        if i.email==y_email:
            a=i.name
            nm.append(a)

            path=i.image
            img.append(str(path).split("/")[-1])

            b=i.id
            ids.append(b)

    s=zip(nm,img,ids)
    return  render(request,'view.html',{'s':s})

# def update(request,id):
#     ak=itemmodel.objects.get(id=id)
#     if request.method=='POST':
#         ak.name=request.POST.get('name')
#         ak.ingree=request.POST.get('ingree')
#         ak.step=request.POST.get('step')
#         ak.image=request.POST.get('image')
#         ak.save()
#         return redirect(request,'s.html')
#     return render(request,'update.html',{'ak':ak})

def update(request, id):
    ak = itemmodel.objects.get(id=id)

    if request.method == 'POST':
        ak.name = request.POST.get('name')
        ak.ingree = request.POST.get('ingree')
        ak.step = request.POST.get('step')
        # ak.type = request.POST.get('type')
        # ak.image = request.FILES.get('image')

        ak.save()
        return render( request,'s.html')

    return render(request, 'update.html', {'ak': ak})
def delete(request,id):
     s=itemmodel.objects.get(id=id)
     s.delete()
     return render(request,'success.html')
     # return redirect(update)
def view2(request):
    data=itemmodel.objects.all()
    nm=[]
    img=[]

    for i in data:
        a=i.name
        nm.append(a)

        path=i.image
        img.append(str(path).split("/")[-1])




    s=zip(nm,img)
    return  render(request,'view1.html',{'s':s})

def details(request, id):
    a = itemmodel.objects.get(id=id)
    # b = profile.objects.get(id=id)
    return render(request, 'details.html', {'a': a})
def emails(request,id):
    a=itemmodel.objects.get(id=id)
    if request.method=='POST':
        sub=contactform(request.POST)
        if sub.is_valid():
            email=sub.cleaned_data['email']
            subject=sub.cleaned_data['subject']
            msg=sub.cleaned_data['message']
            send_mail(subject,msg,EMAIL_HOST_USER,[email],fail_silently=False)
            return render(request,'success.html')
        else:
            return HttpResponse("not valid")

    return render(request,"email.html",{'a':a})




def review(request,id):
    a=itemmodel.objects.get(id=id)
    if request.method=="POST":
        a=review_form(request.POST)
        if a.is_valid():
            i=a.cleaned_data['ids']
            n=a.cleaned_data['name']
            cmt=a.cleaned_data['comment']
            rat=a.cleaned_data['rate']

            b=review_model(ids=i,name=n,comment=cmt,rate=rat)
            b.save()
            return  render(request,'success.html')
        else:
            return HttpResponse("enter valid data")

    return render(request, 'add_review.html',{'a':a})

def viww(request):
    data=itemmodel.objects.all()
    nm=[]
    img=[]
    ids=[]
    for i in data:
        if i.type=="Veg":
            a=i.name
            nm.append(a)

            path=i.image
            img.append(str(path).split("/")[-1])
            d=i.id
            ids.append(d)

    s=zip(nm,img,ids)
    return render(request, 'veg.html', {'s':s})

def viww2(request):
    data=itemmodel.objects.all()
    nm=[]
    img=[]
    ids=[]
    for i in data:
        if i.type=="Non-Veg":
            a=i.name
            nm.append(a)

            path=i.image
            img.append(str(path).split("/")[-1])
            d=i.id
            ids.append(d)

    s=zip(nm,img,ids)
    return render(request, 'veg.html', {'s':s})

# def show(request):
#     j=review_model.objects.get(id=id)
#     return

# def show_review(request,id):
#     j=review_model.objects.get(id=id)
#     return render(request,'show_review.html')

#
# def show_review(request, id):
#     try:
#         j = review_model.objects.get(id=id)
#         return render(request, 'show_review.html', {'j': j})
#     except review_model.DoesNotExist:
#         raise HttpResponse("Review not found")

def show_review(request, id):
    try:

       data = review_model.objects.filter(ids=id)
       nm = []
       c = []
       r = []

       for i in data:
           a = i.name
           nm.append(a)

           p = i.comment
           c.append(p)

           d = i.rate
           r.append(d)

       j = zip(nm, c, r)
       return render(request, 'show_review.html', {'j': j})

    except review_model.DoesNotExist:
        return HttpResponse('<script>alert("Review not found");</script>')

def feedback(request):
    data=itemmodel.objects.all()
    nm=[]
    img=[]
    ids=[]
    for i in data:
        a=i.name
        nm.append(a)

        path=i.image
        img.append(str(path).split("/")[-1])
        d=i.id
        ids.append(d)

    s=zip(nm,img,ids)

    return render(request, '3.html', {'s':s})
