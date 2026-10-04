from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User
# Create your views here.
@method_decorator(csrf_exempt , name="dispatch")
class registerview(View):
    def post(self , request):
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return JsonResponse(
                {"detail":"username and password are required"},
                status =400
            )
        if User.objects.filter(username = username).exists():
            return JsonResponse(
                {"detail":"username already exists"},
                status= 400
            )
        user = User.objects.create_user(
            username=username,
            password=password
        )

        return JsonResponse({
            "message": "User created successfully",
            "username": user.username
        }, status=201)
        

@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):

    def post(self, request):

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:
            return JsonResponse(
                {"detail": "Invalid username or password"},
                status=401
            )

        login(request, user)

        return JsonResponse({
            "message": "Login successful",
            "username": user.username
        })
class PofileView(LoginRequiredMixin , View):
    def get(self , request):
        return JsonResponse({
            "username":request.user.username,
            "is_authenticated" :request.user.is_authenticated
        })