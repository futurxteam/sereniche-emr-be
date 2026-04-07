from django.contrib import admin
from care.emr.models.organization import (
    FacilityOrganization,
    FacilityOrganizationUser,
    Organization,
    OrganizationUser,
)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name", "org_type", "active", "parent")
    search_fields = ("name", "org_type", "external_id")
    list_filter = ("org_type", "active")
    exclude = ("history", "meta", "metadata")


@admin.register(FacilityOrganization)
class FacilityOrganizationAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name", "facility", "org_type", "active", "parent")
    search_fields = ("name", "facility__name", "external_id")
    list_filter = ("org_type", "active")
    exclude = ("history", "meta", "metadata")


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    list_display = ("external_id", "user", "organization", "role")
    search_fields = ("user__username", "organization__name", "external_id")
    list_filter = ("role",)
    exclude = ("history", "meta", "metadata")


@admin.register(FacilityOrganizationUser)
class FacilityOrganizationUserAdmin(admin.ModelAdmin):
    list_display = ("external_id", "user", "organization", "role")
    search_fields = ("user__username", "organization__name", "external_id")
    list_filter = ("role",)
    exclude = ("history", "meta", "metadata")
