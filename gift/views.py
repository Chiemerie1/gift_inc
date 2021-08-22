from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, ConfirmForm, profileform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
import os
from datetime import datetime
from gift_ref.models import ReferralLink
from uuid import uuid4
from .models import ConfirmImage, Profile, Gifters, Gifting, Receiving
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.views import View
from django.utils.http import is_safe_url
from gift_ref.models import ReferralHit, ReferralLink
from gift_ref.settings import COOKIE_HTTPONLY, COOKIE_KEY, COOKIE_MAX_AGE

# Create your views here.


def home(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                #ReferralLink.objects.create(identifier=uuid4(), user_id=request.user.id)
                messages.success(request, "you are now registered as {}".format(username))
                home = redirect("gift:dashboard")
                return home
            else:
                for mssg in form.error_messages:
                    messages.error(request, form.error_messages[mssg])
                
        else:
            for mssg in form.error_messages:
                messages.error(request, form.error_messages[mssg])
    return render(request=request, template_name="gift/home.html",
                                    context={"form": form})


def register(request):
    form = SignupForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Welcome {}, your account has been created".format(username))
            #user = authenticate(username=username, password=password)
            login(request, user)
            ReferralLink.objects.create(identifier=uuid4(), user_id=request.user.id)
            return redirect("gift:dashboard")
            messages.success(request, "You are logged in as {}".format(username))
        else:
            for mssg in form.error_messages:
                messages.error(request, form.error_messages[mssg])
       
    
    form = SignupForm
    return render(request=request, template_name="gift/register.html",
                    context={"form": form})
   


def dashboard(request):

    user_id=request.user.id
    referrals = getRefs(user_id)
    refs = get5Levels(referrals)

    try:
        reflink = ReferralLink.objects.get(user=request.user)
    except ReferralLink.DoesNotExist:
        reflink = ReferralLink.objects.create(user=request.user)
        reflink.save()



    #if request.user.is_authenticated:
    return render(request=request, template_name="gift/dashboard.html",
                    context={"base_url": request.get_host, "ref_url": reflink,
                    "referrals": referrals, "refs":refs,
                    "GIFT": Gifting.objects.all().filter(user=request.user), "RECEIVING": Receiving.objects.all().filter(user=request.user)})
    # else:
    #     return redirect('gift:home')




def get5Levels(referrals):
        for ref in referrals:
            lvl1 = getRefs(ref.hit_user.id)
            if len(lvl1)>0:
                for ref1 in lvl1:
                    lvl2 =  getRefs(ref1.hit_user.id)
                    if len(lvl2)>0:
                        for ref2 in lvl2:
                            lvl3 =  getRefs(ref2.hit_user.id)
                            if len(lvl3)>0:
                                for ref3 in lvl2:
                                    lvl4 =  getRefs(ref3.hit_user.id)
                                    if len(lvl4)>0:
                                        for ref4 in lvl4:
                                            lvl6 =  getRefs(ref4.hit_user.id)
                                            ref4.refs = lvl6
                                    ref3.refs = lvl4
                            ref2.refs = lvl3
                    ref1.refs = lvl2    
            ref.refs = lvl1
        return referrals;

    
def getRefs(user_id):
    try:
        refLink = ReferralLink.objects.get(user_id=user_id)
    except ReferralLink.DoesNotExist:
        refLink = ReferralLink.objects.create(user_id=user_id)
    return refLink.referrals.exclude(hit_user=None)


def profile(request):
  
    try:
        profile = request.user.profile
    except:
        profile = Profile()
        profile.user = request.user
        profile.save()

    form = profileform(request.POST or None,instance=profile)    

    if form.is_valid():
        form.save()
        if form.save():
            messages.success(request, "Your profile has been updated")

    return render(request=request, template_name="gift/profile.html",
                    context={"form": form,
                            "profile": Profile.objects.all().filter(user=request.user)})



def logout_request(request):
    logout(request)
    messages.info(request, "you have been securely logged out")
    home = redirect("gift:home")
    return home


def tree(request):

    user_id=request.user.id
    referrals = getRefs(user_id)
    refs = get5Levels(referrals)

    if request.method == 'POST':
        form =  ConfirmForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            data = upload.save()
            img = form.cleaned_data.get("upload")
            messages.success(request, "uploaded Successfully")

            #form = ConfirmForm()
            return redirect("gift:tree")

    else:
        form = ConfirmForm()
        
    return render(request=request, template_name="gift/tree.html",
                    context={"form": form, "img": ConfirmImage.objects.all(),
                    "referrals": referrals, "refs":refs,})


@login_required
def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("gift:dashboard")
            messages.success(request, message)
        else:
            for mssg in form.error_messages:
                messages.error(request, form.error_messages[mssg])

    return render(request=request, template_name="gift/change_password.html",
                            context={"form": form})