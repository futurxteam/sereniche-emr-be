from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from care.emr.models import (
    Encounter,
    FacilityLocation,
    FacilityLocationEncounter,
    FacilityLocationOrganization,
)
from care.facility.models import Facility


class FacilityLocationResource(resources.ModelResource):
    facility = fields.Field(
        column_name="facility",
        attribute="facility",
        widget=ForeignKeyWidget(Facility, "external_id"),
    )

    parent = fields.Field(
        column_name="parent",
        attribute="parent",
        widget=ForeignKeyWidget(FacilityLocation, "external_id"),
    )

    class Meta:
        model = FacilityLocation
        import_id_fields = ("external_id",)
        exclude = ("facility_organization_cache", "parent_cache")
        fields = (
            "external_id",
            "status",
            "operational_status",
            "system_availability_status",
            "name",
            "description",
            "mode",
            "form",
            "facility",
            "parent",
            "has_children",
            "level_cache",
            "metadata",
            "sort_index",
        )
        export_order = fields


@admin.register(FacilityLocation)
class FacilityLocationAdmin(ImportExportModelAdmin):
    resource_class = FacilityLocationResource
    list_display = (
        "external_id",
        "name",
        "facility",
        "status",
        "operational_status",
        "form",
    )
    search_fields = ("external_id", "name", "status", "form")
    list_filter = ("status", "operational_status", "form", "facility")


@admin.register(FacilityLocationOrganization)
class FacilityLocationOrganizationAdmin(admin.ModelAdmin):
    list_display = ("external_id", "location", "organization")
    search_fields = ("external_id", "location__name", "organization__name")
    list_filter = ("location", "organization")


@admin.register(FacilityLocationEncounter)
class FacilityLocationEncounterAdmin(admin.ModelAdmin):
    list_display = (
        "external_id",
        "location",
        "encounter",
        "status",
        "start_datetime",
        "end_datetime",
    )
    search_fields = ("external_id", "location__name", "encounter__external_id")
    list_filter = ("status", "location", "encounter")
