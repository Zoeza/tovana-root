import os

from django.shortcuts import render, redirect
from .models import Subject, Template, Department, GeneratedReport
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from add_ons import functions
from django.http import HttpResponse, FileResponse
from django.core.files.base import ContentFile
import io


# Create your views here.
def home_manager(request, action):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'
    direction = request.session.get('language')
    nav_side = 'home'

    # -- main page show -- #
    if action == 'main':
        url = direction + "/report_builder/home.html"
        tab = request.session.get('tab')
        request.session['tab'] = None

        context = {
            'nav_side': nav_side,
            'tab': tab,
        }
        return render(request, url, context)


def report_manager(request, action):
    if not request.session.get('language', None):
        request.session['language'] = 'en-us'

    direction = request.session.get('language')
    nav_side = 'report builder'
    departments_list = Department.objects.all()
    subjects_list = Subject.objects.all()
    reports_list = GeneratedReport.objects.all()

    if action == 'report-builder':
        url = direction + "/report_builder/reports/list.html"
        context = {
            'reports_list': reports_list,
            'subjects_list': subjects_list,
            'nav_side': nav_side,
        }
        return render(request, url, context)

    if action == 'add-report':
        url = direction + "/report_builder/reports/add_report.html"
        context = {
            'subjects_list': subjects_list,
            'departments_list': departments_list,
            'nav_side': nav_side,
        }
        return render(request, url, context)

    if action == 'create_nutrition_report':
        data = functions.calculate()
        caffeine_genotype_table = data.get('caffeine_genotype_table')
        caffeine_prs = data.get('caffeine_prs')
        t2d_genotype_table = data.get('t2d_genotype_table')
        t2d_prs = data.get('t2d_prs')
        omega_3_genotype_table = data.get('omega_3_genotype_table')
        omega_3_prs = data.get('omega_3_prs')
        lactose_intolerance_genotype_table = data.get('lactose_intolerance_genotype_table')
        lactose_intolerance_prs = data.get('lactose_intolerance_prs')
        bitter_taste_perception_genotype_table = data.get('bitter_taste_perception_genotype_table')
        bitter_taste_perception_prs = data.get('bitter_taste_perception_prs')
        vitamin_b2_genotype_table = data.get('vitamin_b2_genotype_table')
        vitamin_b2_prs = data.get('vitamin_b2_prs')
        vitamin_b12_genotype_table = data.get('vitamin_b12_genotype_table')
        vitamin_b12_prs = data.get('vitamin_b12_prs')
        vitamin_c_genotype_table = data.get('vitamin_c_genotype_table')
        vitamin_c_prs = data.get('vitamin_c_prs')

        if request.method == 'POST':
            subject_name = request.POST.get('subject_name', False)
            health_care_provider = request.POST.get('health_care_provider', False)
            specimen_type = request.POST.get('specimen_type', False)
            created_at = request.POST.get('created_at', False)
            subject = Subject.objects.get(name=subject_name)
            department = Department.objects.get(health_care_provider=health_care_provider)
            template = Template.objects.get(template_name='Nutrition_Fitness_Wellness')
            template_path = template.template.path
            report = DocxTemplate(template_path)

            context = {
                'Case_OwnerDepartment': department.health_care_provider,
                'Case_MainSample_SourceName': specimen_type,
                'Case_patient': subject.subject_id,
                'Date': created_at,
                'Patient_Name': subject.name,
                'Patient_Gender': subject.gender,
                'Patient_PaternalAncestry': subject.paternal_ancestry,
                'Patient_MaternalAncestry': subject.maternal_ancestry,
                'latest_update_date': created_at,
                'caffeine_genotype_table': caffeine_genotype_table,
                't2d_genotype_table': t2d_genotype_table,
                'omega_3_genotype_table': omega_3_genotype_table,
                'lactose_intolerance_genotype_table': lactose_intolerance_genotype_table,
                'bitter_taste_perception_genotype_table': bitter_taste_perception_genotype_table,
                'vitamin_b2_genotype_table': vitamin_b2_genotype_table,
                'vitamin_b12_genotype_table': vitamin_b12_genotype_table,
                'vitamin_c_genotype_table': vitamin_c_genotype_table,
            }
            report.render(context)
            report_io = io.BytesIO()
            report.save(report_io)
            report_io.seek(0)
            report = ContentFile(report_io.read())

            nutrition_report = GeneratedReport()
            nutrition_report.report.save(subject.subject_id + ' ' + 'Nutrition_Fitness_Wellness.docx', report)
            nutrition_report.report_name = subject.subject_id + ' ' + 'Nutrition_Fitness_Wellness'
            nutrition_report.subject = subject.name
            nutrition_report.created = created_at
            nutrition_report.save()

        return redirect('report-manager', 'report-builder')

    if action == 'delete_report':
        if request.method == 'POST':
            report_id = request.POST.get('report_id', False)
            selected_report = GeneratedReport.objects.all().get(id=report_id)
            selected_report.delete()
        return redirect('report-manager', 'report-builder')

    if action == 'download_report':
        if request.method == 'POST':
            report_id = request.POST.get('report_id', False)
            selected_report = GeneratedReport.objects.all().get(id=report_id)
            return FileResponse(selected_report.report, as_attachment=True)

    if action == 'view_report':
        if request.method == 'POST':
            report_id = request.POST.get('report_id', False)
            selected_report = GeneratedReport.objects.all().get(id=report_id)
            functions.docx_to_pdf('"' + selected_report.report.path + '"', "/tovana-root/site/public/media/reports/")
            pdf_file_path = "/tovana-root/site/public/media/reports/" + selected_report.report_name + ".pdf"
            return FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')
            ##return FileResponse( '"' + selected_report.report.path + '"')
