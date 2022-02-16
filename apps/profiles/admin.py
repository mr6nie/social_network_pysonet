from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import UserNet


class UserNetAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "first_name",
        "last_name",
        "middle_name",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "middle_name",
                    "gender",
                    "birthday",
                )
            },
        ),
        (_("Info"), {"fields": ("avatar", "email", "phone", "github")}),
        (_("Biography"), {"fields": ("bio",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


admin.site.register(UserNet, UserNetAdmin)
