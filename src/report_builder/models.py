from django.db import models
from add_ons import functions


# Create your models here.
class Subject(models.Model):
    subject_id = functions.serial_number_generator(10).upper()
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    paternal_ancestry = models.CharField(max_length=255)
    maternal_ancestry = models.CharField(max_length=255)
    medical_and_surgical_history_summary = models.TextField(max_length=600, default='Not reported.')
    family_history = models.TextField(max_length=600, default='Not reported.')
    csv_file = models.FileField(upload_to='subject/csv_file/', null=True)

    def __str__(self):
        return self.name


class Template(models.Model):
    template_name = models.CharField(max_length=100, default='Nutrition_Fitness_Wellness')
    template = models.FileField(upload_to='templates/', null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.template_name


class Department(models.Model):
    health_care_provider = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', null=True)

    def __str__(self):
        return self.health_care_provider


class GeneratedReport(models.Model):
    objects = None
    created = models.DateTimeField(auto_now_add=True, null=True)
    report_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    report = models.FileField(upload_to='reports/', null=True)
    pdf = models.FileField(upload_to='reports/pdf', null=True)

    class Meta:
        verbose_name = "generated_report"

    def __str__(self):
        return self.report_name
