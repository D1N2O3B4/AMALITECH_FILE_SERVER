from django.shortcuts import redirect
from django.urls import reverse, resolve

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [
            reverse('home'),
            reverse('login'),
            reverse('signup'),
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_complete')
        ]

        # Check if the current path matches the password_reset_confirm pattern
        if resolve(request.path).url_name == 'password_reset_confirm':
            allowed_paths.append(request.path)

        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect(reverse('login'))

        return self.get_response(request)
