from django.contrib import admin
from .models import *

class FileInline(admin.TabularInline):
    model = Method.method_files.through
    extra = 0

class UserInline(admin.TabularInline):
    model = User.methods_liked.through
    extra = 0

class MethodAdmin(admin.ModelAdmin):
    inlines = [FileInline]

class UserAdmin(admin.ModelAdmin):
    inlines = [UserInline]

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Method, MethodAdmin)
admin.site.register(File)
admin.site.register(Semester)
admin.site.register(Aufgaben)
