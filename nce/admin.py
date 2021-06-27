from django.contrib import admin
from nce.models import Project, Department, Feedback


class ProjectAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)

