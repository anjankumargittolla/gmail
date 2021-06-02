"""For using inbuilt User model"""
from django.contrib.auth.models import User

"""To redirect the one page to another page HttpResponseRedirect used"""
from django.http import HttpResponseRedirect, HttpResponse

"""from django.shortcuts import render is used for render the html pages"""
from django.shortcuts import render

"""Registration and Mails are imported to save the data"""
from .models import Registration, Mails

"""auth model has the inbuilt function for login and logout"""
from django.contrib.auth import login, logout, get_user_model

"""From django.contrib.auth.decorators login_required is imported"""
from django.contrib.auth.decorators import login_required

"""MailsForm are imported from forms to enter the data"""
from .forms import MailsForm


# Create your views here.


def home(request):
    """This is for home page"""
    return render(request, "mail/home.html")


def register(request):
    """This will takes to registration page"""
    return render(request, "mail/register.html", {})


def save_reg(request):
    """To save the data in User model and Registration model"""
    if request.method == "POST":
        user = User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST["email"],
            password=request.POST['password'],
            username=request.POST['username'],
        )
        user.set_password('password')
        Registration.objects.create(user=user,
                                    phone=request.POST['phone'],
                                    dob=request.POST['dob'])
        return HttpResponseRedirect("/mail/")
    else:
        return render(request, "mail/register.html", {})


def login_page(request):
    """To go login page to login"""
    return render(request, "mail/login.html", {})


@login_required(login_url='/mail/login/')
def profile(request):
    """This will show the data of the current user email"""
    return render(request, "mail/details.html", {})


def check(request):
    """This view is for check for whether the given email and password is matched or not"""
    usermod = get_user_model()
    if request.method == "POST":
        try:
            user = usermod.objects.get(email=request.POST['email'])
        except usermod.DoesNotExist:
            return HttpResponse('credentials are not correct')
        else:
            if user.check_password(request.POST['password']):
                login(request, user)
                return profile(request)
            else:
                return HttpResponseRedirect("/mail/login/")
    else:
        return render(request, 'mail/login.html', {})


def logout_page(request):
    """This view for logout functionality"""
    logout(request)
    return HttpResponseRedirect('/mail/login/')


def mails(request):
    """TO send the mails from user"""
    if request.method == "POST":
        if request.POST["send"] != "cancel":
            # form = MailsForm(request.POST)
            user = Registration.objects.get(user=request.user)
            Mails.objects.create(sender=user,
                                 receiver=request.POST["receiver"],
                                 subject=request.POST['subject'],
                                 body=request.POST['body'])
            return HttpResponseRedirect("/mail/profile/")
        else:
            user = Registration.objects.get(user=request.user)
            Mails.objects.create(sender=user,
                                 receiver=request.POST["receiver"],
                                 subject=request.POST['subject'],
                                 body=request.POST['body'],
                                 is_draft=True,
                                 )
            return HttpResponseRedirect("/mail/profile/")
    else:
        form = MailsForm()
        return render(request, "mail/compose.html", {"mail": form})


def sender_mails(request):
    """for separating the sent mails and drafts"""
    user = Registration.objects.get(user=request.user)
    sent = Mails.objects.filter(sender=user)
    sent_mail = []
    drafts = []
    for i in sent:
        sent_mail.append(i)
    data = {
        "sent": sent_mail,
    }
    return data
    # return render(request, 'job/drafts.html', {"drafts" : drafts})


def draft_mails(request):
    """This will displays the drafts"""
    user = Registration.objects.get(user=request.user)
    draft = Mails.objects.filter(sender=user, is_draft=True)
    print(draft, request.user.first_name)
    return render(request, 'mail/drafts.html', {"draft": draft})


def sent_mails(request):
    """This will displays the sent emails"""
    return render(request, 'mail/sent.html', {"data": sender_mails(request)})


def receive_mails(request):
    # import pdb
    # pdb.set_trace()
    user = request.user
    spam = Mails.objects.filter(receiver=user.email)
    spam_mail=[]
    inbox_mails = []
    for i in spam:
        new = User.objects.get(first_name=i.sender)
        reg = Registration.objects.get(user=new)
        if reg.is_spam:
            spam_mail.append(i)
        else:
            inbox_mails.append(i)
        new_data = {
            "inbox" : inbox_mails,
            "spam" : spam_mail
        }
        return new_data


def inbox(request):
    """This will displays the inbox emails"""
    return render(request, 'mail/inbox.html', {"data": receive_mails(request)})


def spam_mails(request):
    return render(request, 'mail/spam.html', {"data": receive_mails(request)})
