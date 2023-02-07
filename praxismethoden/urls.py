from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("timeline", views.timeline, name="timeline"), 
    path("alle", views.alle, name="alle"), 
    path("meine", views.meine, name="meine"),
    path("course", views.course, name="course"),
    path("methoden/<int:method_id>", views.method_single, name="method_single"), # single method view
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # staff only
    path("staff", views.staff_view, name="staff"),
    path("methoden/<int:method_id>/edit", views.method_single_edit, name="method_single_edit"),
    path("methoden/<int:method_id>/edit/file", views.method_single_edit_file, name="method_single_edit_file"),
    path("methoden/new", views.new_method, name="new_method"),

    # api routes
    path("api/methoden/<int:method_id>", views.api_method_single, name="api_method_single"),
    path("api/methoden/<str:category>", views.category, name="category"),
    path("api/all_categories", views.all_categories, name="all_categories"),
    path("api/all_methods", views.all_methods, name="all_methods"),
]