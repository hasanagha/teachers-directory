from django.contrib import admin

from account.models import Teacher, Subject
from account.forms import TeacherForm


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'created_on', 'updated_on')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_active', 'created_on', 'updated_on')
    list_filter = ('is_active',)
    search_fields = ('subject',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)

admin.site.site_header = "Teachers Directory"
admin.site.site_title = "Teachers Directory"
admin.site.index_title = "Welcome to Teachers Directory Admin"
