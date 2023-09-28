from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import SignupForm, LoginForm
import random
# Create your views here.

#@login_required(login_url='login')

def home(request):
    std=Student.objects.all()
    context={
        'std':std,
    }
    return render(request,'student/home.html',context)

def add_student(request):
    std=Student.objects.all()
    
    if request.method=='POST' and 'img' in request.FILES and 'resume' in request.FILES:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        city=request.POST.get('city')
        img=request.FILES['img']
        resume=request.FILES['resume']

        std=Student(
        name=name,
        email=email,
        password=password,
        phone=phone,
        gender=gender,
        city=city,
        Img=img,
        Resume=resume,
        )        
        std.save() 
        return redirect('home')            
    return render(request,'student/add_student.html')

def delete_student(request,id):
    s=Student.objects.get(pk=id)
    s.delete()
    return redirect('home')

def update_student(request, id):
    std = Student.objects.get(pk=id)
    
    if request.method == "POST":
        std.name=request.POST.get('name')
        std.email=request.POST.get('email')
        std.password=request.POST.get('password')
        std.phone=request.POST.get('phone')
        std.gender=request.POST.get('gender')
        std.city=request.POST.get('city')

        img=request.FILES.get('img')
        resume=request.FILES.get('resume')
        
        if img:
            std.Img = img
        if resume:
            std.Resume = resume  

        std.save()
        return redirect('home')
    return render(request,'student/update_student.html',{'std':std})


##########################################################################################################


def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            otp = str(random.randint(100000, 999999))
            user = User(name=form.cleaned_data['name'],
                        email=form.cleaned_data['email'],
                        mobile_number=form.cleaned_data['mobile_number'],
                        otp=otp)
            user.save()

            subject = 'Verify Your Email'
            message = f'Your OTP for email verification: {otp}'
            from_email = 'tarun97thakur@gmail.com'
            to_email = [form.cleaned_data['email']]
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            return redirect('email')
    else:
        form = SignupForm()
    
    return render(request, 'student/signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_verified:
                    login(request, user)
                    return redirect('signup')  
                else:
                    return render(request, 'student/login.html', {'form': form, 'error': 'Email is not verified'})
            else:
                return render(request, 'student/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    
    return render(request, 'student/login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')


#####################################################################################################

#def signup_page(request):
#    if request.method=='POST':
#        form=UserRegisterForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username=form.cleaned_data.get('username')
#            email=form.cleaned_data.get('email')
#            ################# Mail System #################
#            htmly=get_template('user/email.html')
#            d={'username':username}
#            subject, from_email, to = 'welacome', 'tarun97thakur@gmail.com', email
#            html_content=htmly.render(d)
#            msg=EmailMultiAlternatives(subject, html_content, from_email, [to])
#            msg.attach_alternative(html_content, "text/html")
#            msg.send()
#
#            messages.success(request, f'Your account has been created ! You are now able to log in')
#            return redirect('login')
#        else:
#            form = UserRegisterForm()
#    return render(request, 'user/register.html', {'form': form})
#        
#   #     uname=request.POST.get('username')
#   #     email=request.POST.get('email')
#   #     pass1=request.POST.get('pass1')
#   #     pass2=request.POST.get('pass2')
#
#   #     if pass1!=pass2:
#   #         messages.warning(request,"Your password and confrom password are not Same!!!")
#   #     else:
#   #         my_user=User.objects.create_user(uname,email,pass1)
#   #         my_user.save()
#   #         return redirect('login')
#   # return render(request, 'student/signup.html')
#
#def login_page(request):
#    if request.method == 'POST':
#  
#        # AuthenticationForm_can_also_be_used__
#  
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username = username, password = password)
#        if user is not None:
#            form = login(request, user)
#            messages.success(request, f' Welcome {username} !!')
#            return redirect('home')
#        else:
#            messages.info(request, f'Account done not exit plz sign in')
#    form = AuthenticationForm()
#    return render(request, 'student/login.html', {'form':form})
#
#
#  # if request.method=='POST':
#  #     username=request.POST.get('username')
#  #     pass1=request.POST.get('pass')
#  #     user=authenticate(request,username=username,password=pass1)
#  #     if user is not None:
#  #         login(request,user)
#  #         return redirect('home')
#  #     else:
#  #         messages.warning(request,"Username or Password is incorrect!!!")
#  # return render(request, 'student/login.html')
#
#def logout_page(request):
#    logout(request)
#    return redirect('login')



