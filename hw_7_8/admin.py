from django.contrib import admin
from hw_7_8.models import Category, Task, SubTask
from django.db.models import QuerySet

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'status', 'deadline')
    search_fields = ('title',)
    list_filter = ('status', 'deadline')
    list_per_page = 2
    inlines = [SubTaskInline]

    def short_title(self, obj: Task) -> str:
        return f"{obj.title[:10]}..."


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'deadline')
    list_filter = ('title', 'status','deadline')
    list_per_page = 2
    search_fields = ('title',)

    actions = ['update_status_to_done']

    def update_status_to_done(self, request, objects: QuerySet) -> None:
        for obj in objects:
            obj.status = 'Done'

            obj.save()

    update_status_to_done.short_description = "Change status to Done"


class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


# admin.site.register(Task)
#admin.site.register(SubTask)
admin.site.register(Category)