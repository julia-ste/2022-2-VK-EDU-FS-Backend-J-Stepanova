from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from utils.form_utils import add_field_placeholders


@require_http_methods(["GET"])
def home(request):
    return render(request, "home.html")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        form = add_field_placeholders(form)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                return redirect("home")
        return render(
            request,
            "login.html",
            context={"login_form": form, "error": "Invalid username or password"},
        )
    form = AuthenticationForm()
    form = add_field_placeholders(form)
    return render(request, "login.html", context={"login_form": form})
