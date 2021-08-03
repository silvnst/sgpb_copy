import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Category, User, Method

# Create your views here.

def index(request):
    cards = Method.objects.all()
    return render(request, "praxismethoden/index.html", {
        "cards": cards
    })

def finden(request):
    return render(request, "praxismethoden/finden.html")

@login_required
def meine(request):
    cards = Method.objects.filter(likes=request.user)
    return render(request, "praxismethoden/meine.html", {
        "cards": cards
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "praxismethoden/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "praxismethoden/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "praxismethoden/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "praxismethoden/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "praxismethoden/register.html")

def method_single(request, method_id):

    # Query for requested email
    try:
        m = Method.objects.get(pk=method_id)
    except Method.DoesNotExist:
        return JsonResponse({"error": "Method not found."}, status=404)

    # Return email contents
    if request.method == "GET":
        return JsonResponse(m.serialize())

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

def all_categories(request):
    
    all_cat = Category.objects.all()
    return JsonResponse([cat.serialize() for cat in all_cat], safe=False)

def category(request, category):

    try:
        cat = Category.objects.get(name_lower=category.lower())
    except Method.DoesNotExist:
        return JsonResponse({"error": "Method not found."}, status=404)

    methods = Method.objects.filter(category=cat)
    return JsonResponse([method.serialize() for method in methods], safe=False)
    