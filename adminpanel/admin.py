from django.contrib import admin

# Register your models here.
from .models import UserMentorMe, Education, Career, EmailTemplates, AdminNotes


class CareersInline(admin.TabularInline):
    model = Career
    fields = ("companyname", "fieldofwork", "iscurrent", 
              "jobtitle", "startdate", "enddate",
              "location", "position",)
    readonly_fields = ['inserted_at', 'updated_at']

    extra = 0


class EducationsInline(admin.TabularInline):
    model = Education
    fields = ("degreetype", "institutionname", 
              "location", "institutiontype", 
              "graduationdate", "iscurrent",
              "domainofstudy",)
    readonly_fields = ['inserted_at', 'updated_at']
    extra = 0

class AdminNotesInline(admin.TabularInline):
    model = AdminNotes
    fields = ("text_notes", "inserted_at", "updated_at",)
    readonly_fields = ['inserted_at', 'updated_at']
    extra = 0

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', "lastname", "email", 'mentorapprovalrequest',
                    'approvedasmentor', 'email_verified', 'inserted_at', 'updated_at')
    exclude = ('password_hash',)
    list_filter = ('mentorapprovalrequest', 'approvedasmentor', 'email_verified')
    search_fields = ('firstname', "lastname", "email")
    readonly_fields = ['inserted_at', 'updated_at']
    inlines = [
        AdminNotesInline, CareersInline, EducationsInline
    ]

    def degreetype(self, obj):
        degreetype_education = Education.objects.filter(user=obj.id).last()
        if degreetype_education is not None:
            return degreetype_education.degreetype
        else:
            return ""

    def iscurrent(self, obj):
        iscurrent_education = Education.objects.filter(user=obj.id).last()
        if iscurrent_education is not None:
            return iscurrent_education.iscurrent
        else:
            return ""

    def domainofstudy(self, obj):
        domainofstudy_education = Education.objects.filter(user=obj.id).last()
        if domainofstudy_education is not None:
            return domainofstudy_education.iscurrent
        else:
            return ""

    def companyname(self, obj):
        companyname_career = Career.objects.filter(user=obj.id).last()
        if companyname_career is not None:
            return companyname_career.companyname
        else:
            return ""

    def fieldofwork(self, obj):
        fieldofwork_career = Career.objects.filter(user=obj.id).last()
        if fieldofwork_career is not None:
            return fieldofwork_career.fieldofwork
        else:
            return ""


class EmailTemplatesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)


admin.site.register(UserMentorMe, UserProfileAdmin)
admin.site.register(EmailTemplates, EmailTemplatesAdmin)
