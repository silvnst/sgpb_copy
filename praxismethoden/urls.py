from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("finden", views.finden, name="finden"),
    path("meine", views.meine, name="meine"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # api routes
    path("api/methoden/<int:method_id>", views.method_single, name="method_single"),
    path("api/methoden/<str:category>", views.category, name="category"),
    path("api/all_categories", views.all_categories, name="all_categories"),
]