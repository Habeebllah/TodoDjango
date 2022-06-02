from django.contrib import admin
from app.models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "status",
        "created_at",
        "updated_at",     
    ]
    date_hierarchy = "created_at"