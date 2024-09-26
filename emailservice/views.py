
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from .forms import UserRegistrationForm, LoginForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

def logout_view(request):
    logout(request)
    return redirect('login')














def login_view(request):
    print("Login view accessed")
    if request.method == 'POST':
        print("POST request received")
        form = LoginForm(request.POST)
        print("Form created")
        if form.is_valid():
            print("Form is valid")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Email:", email)
            print("Password:", password)
            try:
                user = User.objects.get(email=email)
                print("User found")
                if check_password(password, user.password):
                    print("Password correct")
                    login(request, user)
                    print("Login successful")
                    return redirect('dashboard')
                else:
                    print("Password incorrect")
                    messages.error(request, 'Invalid email or password.')
            except User.DoesNotExist:
                print("User not found")
                messages.error(request, 'Invalid email or password.')
    else:
        print("GET request received")
        form = LoginForm()
    print("Rendering login template")
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.user.email
        recipient_list = [email.strip() for email in request.POST['recipient_list'].split(',')]

        # Basic validation
        if not all([subject, message, from_email, recipient_list]):
            messages.error(request, "All fields are required.")
            return render(request, 'send_email.html')

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Email sent successfully.')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Email sending failed: {str(e)}')
            return render(request, 'send_email.html')
    return render(request, 'send_email.html')


#
# @login_required
# def send_email(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         # Basic validation
#         if not all([email, subject, message]):
#             messages.error(request, "All fields are required.")
#             return render(request, 'email_template.html')
#
#         send_email_status = send_mail(
#             subject,
#             message,
#             None,  # Uses DEFAULT_FROM_EMAIL from settings
#             [email],
#             fail_silently=False,
#         )
#
#         if send_email_status == 1:
#             messages.success(request, "Email sent successfully!")
#             return redirect(reverse('success_url'))
#         else:
#             messages.error(request, "Email sending failed!")
#             return redirect(reverse('error_url'))
#     else:
#         return render(request, 'email_template.html')

@login_required
def email_template(request):
    return render(request, 'email_template.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def email_success(request):
    return render(request, 'email_success.html')

def email_error(request):
    return render(request, 'email_error.html')

def home(request):
    return render(request, 'home.html')
