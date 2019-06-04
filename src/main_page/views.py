from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Siteuser
from .forms import Signupform,Loginform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return HttpResponse("This is the main page")
class LoginView(TemplateView):
    template_name = 'main_page/loginex.html'
class SignupView(TemplateView):
    template_name='main_page/signup.html'

def signupnew(request):
    uservalue=request.POST.get("username","")
    passwordvalue1=request.POST.get("password1","") or None
    passwordvalue2=request.POST.get("password2","") or None

    if passwordvalue1==passwordvalue2:
        try:
            user= Siteuser.objects.get(username=uservalue) #if able to get, user exists and must try another username
            context= {'error':'The username you entered has already been taken. Please try another username.'}
            return render(request, 'main_page/signup.html', context)
        except Siteuser.DoesNotExist:
            user=Siteuser(username=uservalue,password1=passwordvalue1,password2=passwordvalue2)
            user.save()
            login(request,user)
            return render(request, 'main_page/login.html')
    else:
        context= {'error':'The passwords that you provided don\'t match'}
        return render(request, 'main_page/signup.html', context)

def signup(request):
    uservalue=''
    passwordvalue1=''
    passwordvalue2=''

    form= Signupform(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password1")
        passwordvalue2= form.cleaned_data.get("password2")
        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'main_page/signup.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(uservalue, password= passwordvalue1)
                user.save()
                login(request,user)
                fs.user= request.user

                fs.save()
                context= {'form': form}
                return render(request, 'main_page/signup.html', context)
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'main_page/signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'main_page/signup.html', context)

def pageloginnew(request):
  
    uservalue=request.POST.get("username")
    passwordvalue=request.POST.get("password")

    user= authenticate(username=uservalue, password=passwordvalue)
    if user is not None:
        login(request, user)
        context= {
                  'error': 'The login has been successful'}
        
        return render(request, 'main_page/login.html', context)
    else:
        context= {
                  'error': 'The username and password combination is incorrect'}
        
        return render(request, 'main_page/login.html', context )

def pagelogin(request):
  
    uservalue=''
    passwordvalue=''

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'main_page/login.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'main_page/login.html', context )

    else:
        context= {'form': form}
        return render(request, 'main_page/login.html', context)
