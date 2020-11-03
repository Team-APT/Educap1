from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime
import hashlib
from .models import *
from quiz.models import *
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def explore(request):
    dict={}
    for obj in Category.objects.all():
        dict[obj.streamname]={}
    for obj in Category.objects.all():
        for objec in SubCategory.objects.all().filter(category=obj.id):
            dict[obj.streamname][objec.sub_category]=[]
    for obj in Category.objects.all():
        for objec in SubCategory.objects.all().filter(category=obj.id):
            for object in Course.objects.all().filter(substreamid=objec.id):
                dict[obj.streamname][objec.sub_category].append(object)
    return render(request,'explore.html',{'dict':dict})

def explore_colleges(request,courseid):
    array,arr,ar=[],[],[]
    for obj in Collegesofcourse.objects.all().filter(courseid=courseid):
        ar.append(obj)
    for elem in ar:
        name=elem.collegename
        array=College.objects.all().filter(collegename=name)
        for item in array:
            arr.append(item)
    if request.user.is_authenticated:
        return render(request,'colleges2.html',{'arr':arr})
    else:
        return render(request,'colleges1.html',{'arr':arr})

def all_colleges(request):
    arr=College.objects.all()
    if request.user.is_authenticated:
        return render(request,'colleges2.html',{'arr':arr})
    else:
        return render(request,'colleges1.html',{'arr':arr})


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile',username=request.user.username)
    elif request.method == 'POST':
        try:
            saverecord=User()
            saverecord.username=request.POST.get('username')
            saverecord.first_name=request.POST.get('first_name')
            saverecord.last_name=request.POST.get('last_name')
            saverecord.email=request.POST.get('email')
            saverecord.contact=request.POST.get('contact')
            saverecord.password=make_password(request.POST.get('password'))
            saverecord.date_joined=datetime.now()
            saverecord.save()
            messages.success(request,"Account Created Successfully.Please login to continue.")
            return redirect('auth_login')
        except IntegrityError:
            messages.error(request,"The User Already exists!!")
            return render(request,'signup.html')
    else:
        return render(request, 'signup.html')

def auth_login(request):
    if request.user.is_authenticated:
        return redirect('profile',username=request.user.username)
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            get_user=User.objects.get(username=username)
            if get_user.check_password(password):
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('profile',username=username)
                else:
                    messages.error(request,'Username or Password is incorrect')
                    return render(request,'login.html')
            else:
                messages.error(request,'Password is incorrect')
                return render(request,'login.html')
        except User.DoesNotExist:
            messages.error(request,'User does not exist')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def auth_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request,username):
    user = User.objects.all().filter(username=username)
    if not user.exists():
        return redirect('home')
    return render(request,'profile.html',{'user':user})

@login_required
def change_password(request,username):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,'Your password was successfully updated!')
            return redirect('change_password',username=username)
        else:
            messages.error(request,'Entered Data is incorrect.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form': form})

@login_required
def test1(request,username):
    return render(request,'test1.html')

@login_required
def test2(request,username):
    return render(request,'test2.html')

@login_required
def wishlist(request,username):
    wish=WishlistItem.objects.all().filter(user=username)
    arr=[]
    for obj in wish:
        id=obj.item
        clg=College.objects.get(collegeid=id)
        arr.append(clg)
    return render(request,'wishlist.html',{'arr': arr})

@login_required
def test_result(request,username):
    user=User.objects.get(username=username)
    x=max(user.step1,user.step2,user.step3,user.step4)
    if(x==user.step1):
        num=1
    elif(x==user.step2):
        num=2
    elif(x==user.step3):
        num=3
    elif(x==user.step4):
        num=4
    array=[]
    for obj in SubCategory.objects.all().filter(category=num):
        for subobj in Course.objects.all().filter(substreamid=obj.id):
            array.append(subobj)
    return render(request,'results.html',{'array':array})

@login_required
def colleges(request,username,courseid):
    array,arr,ar=[],[],[]
    for obj in Collegesofcourse.objects.all().filter(courseid=courseid):
        ar.append(obj)
    for elem in ar:
        name=elem.collegename
        array=College.objects.all().filter(collegename=name)
        for item in array:
            arr.append(item)
    return render(request,'colleges2.html',{'arr':arr})

@login_required
def add_wishlist(request,collegeid):
    try:
        wish=WishlistItem()
        inst=College.objects.get(collegeid=collegeid)
        wish.item=inst.collegeid
        wish.user=request.user.username
        wish.created=datetime.now()
        wish.save()
        context={
        'msg':"College successfully added to the wishlist"
        }
        return render(request,'confirm.html',context)
    except IntegrityError:
        context={
        'msg':"College already added to the wishlist"
        }
        return render(request,'confirm.html',context)

@login_required
def remove_wishlist(request,collegeid):
    wish=WishlistItem.objects.get(item=collegeid,user=request.user.username)
    wish.delete()
    context={
    'msg':"College removed from the wishlist"
    }
    return render(request,'confirm.html',context)

@login_required
def consult(request,username):
    try:
        if request.method=="POST":
            obj=PhoneConsult()
            obj.username=request.POST.get('username')
            obj.contact=request.POST.get('contact')
            obj.save()
            context={
            'msg':"Phone number successfully registered for consultation. We will contact you for career consultation within one week. Further details will be intimated via mail."
            }
            return render(request,'consult.html',context)
    except IntegrityError:
        context={
        'msg':"Already registered!"
        }
        return render(request,'consult.html',context)
    return render(request,'consult.html')
