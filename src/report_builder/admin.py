from django.contrib import admin
from .models import Subject, Template, Department, GeneratedReport

admin.site.register(Subject)
admin.site.register(Template)
admin.site.register(Department)
admin.site.register(GeneratedReport)
