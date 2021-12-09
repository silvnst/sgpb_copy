from django.contrib import admin
from .models import *



admin.site.register(User)
admin.site.register(Category)
admin.site.register(Method)
admin.site.register(File)
#admin.site.register(Course)
admin.site.register(Module)


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 0
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]