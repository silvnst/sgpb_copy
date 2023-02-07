import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.core.checks.messages import Error
from django.db import IntegrityError
from django.forms import HiddenInput, fields, formset_factory
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import Category, File, User, Method
from .forms import MethodForm, FileForm
from django.contrib.admin.views.decorators import staff_member_required

# Course View and Admin

def course(request):
    course = request.user.students.last()

    return render(request, "praxismethoden/course.html", {
        "course": course
    })

# Hauptseiten

def index(request):
    return render(request, "praxismethoden/index.html", {
        
    })

def timeline(request):
    return render(request, "praxismethoden/timeline.html")

def alle(request):
    cards = Method.objects.all()
    categories = Category.objects.all()
    return render(request, "praxismethoden/methodenansicht.html", {
        "seiten_titel": "Methoden",
        "cards": cards,
        "categories": categories,
        "titel": "Alle Methoden",
        "untertitel": "Hier findest du die aktuellen Methoden der Projektbox. Mit deinem Feedback werden sie laufend aktualisiert."
    })

@login_required(login_url='login')
def meine(request):
    cards = Method.objects.filter(likes=request.user)
    return render(request, "praxismethoden/methodenansicht.html", {
        "seiten_titel": "Favoriten",
        "cards": cards,
        "titel": "Favoriten",
        "untertitel": "Hier findest du deine favoritisierten Methoden."
    })

def method_single(request, method_id):
    m = Method.objects.get(pk=method_id)
    # f = m.method_files.all()
    return render(request, "praxismethoden/single_methodenansicht.html", {
        "method": m
    })

# Staff Member Views

@staff_member_required()
def staff_view(request):

    m = Method.objects.all()
    u = User.objects.filter(is_staff=False)
    return render(request, "praxismethoden/staff/overview.html", {
        "titel": "Betreuenden Ansicht",
        "all_methods": m,
        "users": u
    })
        
@login_required(login_url='login')
def method_single_edit(request, method_id):

    if request.user.is_staff:
        m = Method.objects.get(pk=method_id)
        f = MethodForm(instance=m)
        files_formset = modelformset_factory(
            File, form = FileForm, can_delete = True,
        )
        if request.method == "POST":
            f = MethodForm(request.POST, instance=m)
            if f.is_valid():
                f.save()
                return render(request, "praxismethoden/staff/single_edit_methodenansicht.html", {
                    "id": method_id,
                    "form": f,
                    "file_form": files_formset,
                    "method": m
                })
        else:
            return render(request, "praxismethoden/staff/single_edit_methodenansicht.html", {
                "id": method_id,
                "form": f,
                "file_form": files_formset,
                "method": m
            })
    else:
        return HttpResponseRedirect(reverse("method_single", kwargs={'method_id': method_id})) 

@staff_member_required()
def method_single_edit_file(request, method_id):
    if request.method == "POST":
        files_formset = modelformset_factory(File, fields="__all__", can_delete=True)
        formset = files_formset(request.POST, request.FILES)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
            for i in instances:
                i.save()
            return HttpResponseRedirect(reverse("method_single_edit", kwargs={'method_id': method_id}))
        else:
            print(formset.errors)
            return HttpResponseRedirect(reverse("method_single_edit", kwargs={'method_id': method_id}))
    else:
        return HttpResponseRedirect(reverse("method_single_edit", kwargs={'method_id': method_id}))

@staff_member_required()
def new_method(request):
    f = MethodForm()
    if request.method == "POST":
        f = MethodForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse("staff"))
        else:
            return render(request, "praxismethoden/staff/new_method.html", {
                "form": f,
            })
    else:
        return render(request, "praxismethoden/staff/new_method.html", {
                "form": f,
            })

@staff_member_required()
def method_delete(request, method_id):
    m = Method.objects.get(pk=method_id)
    m.delete()
    return redirect("staff")

# account

def email_check(user):
    return user.email.endswith('unisg.ch')

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
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "praxismethoden/register.html", {
                "message": "Passwörter müssen übereinstimmen."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "praxismethoden/register.html", {
                "message": "Diese E-Mail ist schon vergeben."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "praxismethoden/register.html")


# api

def api_method_single(request, method_id):

    # Query for requested method
    try:
        m = Method.objects.get(pk=method_id)
    except Method.DoesNotExist:
        return JsonResponse({"error": "Method not found."}, status=404)

    # Return method contents
    if request.method == "GET":
        return JsonResponse(m.serialize())

    elif request.method == "POST":
        data = json.loads(request.body)
        if data.get("like") == True:
            m.likes.remove(request.user)
        else:
            m.likes.add(request.user)
        m.save()
        return HttpResponse(status=204)

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

def all_methods(request):
    
    all_m = Method.objects.all()
    return JsonResponse([m.serialize() for m in all_m], safe=False)

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
    