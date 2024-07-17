from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.views import LoginView


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"Account created for {email}")
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
