from django.contrib import admin
from care.emr.models.organization import (
    FacilityOrganization,
    FacilityOrganizationUser,
    Organization,
    OrganizationUser,
)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "org_type", "active", "parent")
    search_fields = ("name", "org_type")
    list_filter = ("org_type", "active")


@admin.register(FacilityOrganization)
class FacilityOrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "facility", "org_type", "active", "parent")
    search_fields = ("name", "facility__name")
    list_filter = ("org_type", "active")


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role")
    search_fields = ("user__username", "organization__name")
    list_filter = ("role",)
    exclude = ("meta", "history", "metadata") # This will hide the red boxes!


@admin.register(FacilityOrganizationUser)
class FacilityOrganizationUserAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role")
    search_fields = ("user__username", "organization__name")
    list_filter = ("role",)
    exclude = ("meta", "history", "metadata") # This will hide the red boxes!
