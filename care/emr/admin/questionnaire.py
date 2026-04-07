from django.contrib import admin
from care.emr.models.questionnaire import (
    Questionnaire,
    QuestionnaireTag,
    FormSubmission,
    QuestionnaireResponse,
    QuestionnaireOrganization,
    QuestionnaireFacilityOrganization,
    QuestionnaireResponseTemplate,
)

@admin.register(QuestionnaireTag)
class QuestionnaireTagAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name", "slug")
    search_fields = ("name", "slug", "external_id")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("external_id", "title", "slug", "version", "status", "subject_type")
    search_fields = ("title", "slug", "external_id")
    list_filter = ("status", "subject_type")
    readonly_fields = ("external_id", "organization_cache", "internal_organization_cache")
    # We exclude the caches from the 'editable' fields to avoid 'This field is required' errors
    exclude = ("history", "meta", "metadata", "organization_cache", "internal_organization_cache")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["styling_metadata"].initial = {}
        form.base_fields["questions"].initial = []
        form.base_fields["version"].initial = "1.0"
        form.base_fields["status"].initial = "active"
        form.base_fields["subject_type"].initial = "encounter"
        return form

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("external_id", "questionnaire", "patient", "status")
    search_fields = ("external_id", "patient__external_id")
    list_filter = ("status", "questionnaire")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ("external_id", "questionnaire", "patient", "encounter", "status")
    search_fields = ("external_id", "patient__external_id", "encounter__external_id")
    list_filter = ("status", "questionnaire")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")

@admin.register(QuestionnaireOrganization)
class QuestionnaireOrganizationAdmin(admin.ModelAdmin):
    list_display = ("external_id", "questionnaire", "organization")
    search_fields = ("questionnaire__title", "organization__name", "external_id")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")

@admin.register(QuestionnaireFacilityOrganization)
class QuestionnaireFacilityOrganizationAdmin(admin.ModelAdmin):
    list_display = ("external_id", "questionnaire", "organization")
    search_fields = ("questionnaire__title", "organization__name", "external_id")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")

@admin.register(QuestionnaireResponseTemplate)
class QuestionnaireResponseTemplateAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name", "facility", "questionnaire")
    search_fields = ("name", "facility__name", "questionnaire__title", "external_id")
    list_filter = ("facility", "questionnaire")
    readonly_fields = ("external_id",)
    exclude = ("history", "meta", "metadata")
