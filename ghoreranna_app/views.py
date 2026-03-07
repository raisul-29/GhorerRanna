from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Menu
from .forms import RegistrationForm, LoginForm, MenuForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash password before saving to DB
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            try:
                user = User.objects.get(email=email)
                # Verify hashed password
                if check_password(password, user.password):
                    if user.status == 'Active':
                        # Set manual session variables because we aren't using Django's built-in User model
                        request.session['user_id'] = user.user_id
                        request.session['user_role'] = user.role
                        request.session['user_name'] = user.name
                        messages.success(request, f"Welcome back, {user.name}!")
                        return redirect('home')
                    else:
                        messages.error(request, "Your account is inactive. Please contact support.")
                else:
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    request.session.flush() # Clear the session data
    messages.success(request, "You have been logged out.")
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')