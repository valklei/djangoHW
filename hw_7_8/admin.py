from django.contrib import admin
from hw_7_8.models import Category, Task, SubTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'categories__name', 'deadline', 'status')
    list_filter = ('title', 'categories__name', 'deadline', 'status')
    list_per_page = 2


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'deadline')
    list_filter = ('title', 'status','deadline')
    list_per_page = 2



# admin.site.register(Task)
#admin.site.register(SubTask)
admin.site.register(Category)