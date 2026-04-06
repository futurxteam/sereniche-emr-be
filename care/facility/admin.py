from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from care.facility.models import Facility
from django.contrib.auth import get_user_model

User = get_user_model()

class FacilityResource(resources.ModelResource):
    created_by = fields.Field(
        column_name="created_by",
        attribute="created_by",
        widget=ForeignKeyWidget(User, "username"),
    )

    class Meta:
        model = Facility
        import_id_fields = ("external_id",)
        exclude = ("geo_organization_cache", "internal_organization_cache")
        fields = (
            "external_id",
            "name",
            "facility_type",
            "is_active",
            "verified",
            "pincode",
            "address",
            "phone_number",
            "created_by",
        )
        export_order = fields


@admin.register(Facility)
class FacilityAdmin(ImportExportModelAdmin):
    resource_class = FacilityResource
    list_display = ("external_id", "name", "facility_type", "is_active", "verified")
    search_fields = ("external_id", "name", "pincode", "address")
    list_filter = ("facility_type", "is_active", "verified")
