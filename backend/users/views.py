from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({"message": "Login successful", "is_admin": user.is_staff})
        else:
            return Response({"message": "Login failed"}, status=401)


class SignupView(View):
    @csrf_exempt
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
        return render(request, "signup.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
