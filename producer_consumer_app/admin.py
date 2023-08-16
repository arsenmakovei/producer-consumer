from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from producer_consumer_app.models import Employee, Order


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "probation",
        "position",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "probation",
                    "position",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "probation",
                    "position",
                )
            },
        ),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "task_id", "description", "employee"]
