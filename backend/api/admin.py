from django.contrib import admin

from .models import *

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class EmailSubstringAdmin(admin.ModelAdmin):
    list_display = ('institution', 'substring')

class IdFormatAdmin(admin.ModelAdmin):
    list_display = ('institution', 'regex')

class CourseCodeFormatAdmin(admin.ModelAdmin):
    list_display = ('institution', 'regex')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'description')

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'first_name',
                    'institution',
                    'email',
                    'user_id')

class SessionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NewtAdmin(admin.ModelAdmin):
    list_display = ('course',
                    'newt_code',
                    'session_type',
                    'start',
                    'finish',
                    'message')

class PingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Ping, PingAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(EmailSubstring, EmailSubstringAdmin)
admin.site.register(IdFormat, IdFormatAdmin)
admin.site.register(CourseCodeFormat, CourseCodeFormatAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(SessionType, SessionTypeAdmin)
admin.site.register(Newt, NewtAdmin)


