from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            confirmation_token = default_token_generator.make_token(user)
            confirmation_link = f"http://localhost:8000/confirm/{user.id}/{urlsafe_base64_encode(force_bytes(confirmation_token))}/"

            send_mail(
                subject="Confirm Your Email",
                message=f"Click the link below to confirm your email:\n{confirmation_link}",
                from_email=settings.SERVER_EMAIL,
                recipient_list=[user.email],
            )
            messages.success(request, f"Account created for {user.email}. Please check your email for confirmation.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm

def confirm_email(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
    except User.DoesNotExist:
        messages.error(request, "User not found.")
    return redirect('login')



