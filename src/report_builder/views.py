import os

from django.shortcuts import render, redirect
from .models import Subject, Template, Department, GeneratedReport
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from add_ons import functions
from . import report_actions

import subprocess
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

    if action == 'choose_report':
        if request.method == 'POST':
            if request.POST.get('report_name') == 'Nutrition_Fitness_Wellness':
                url = direction + "/reports/reports/add_report.html"

                context = {
                    'subjects_list': subjects_list,
                    'departments_list': departments_list,
                    'nav_side': nav_side,

                }
                return render(request, url, context)
            else:
                redirect('home-manager', 'main')
        redirect('report-manager', 'report-builder')

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
        exercise_behavior_genotype_table = data.get('exercise_behavior_genotype_table')
        exercise_behavior_prs = data.get('exercise_behavior_prs')
        power_and_strength_genotype_table = data.get('power_and_strength_genotype_table')
        power_and_strength_prs = data.get('power_and_strength_prs')
        endurance_training_genotype_table = data.get('endurance_training_genotype_table')
        endurance_training_prs = data.get('endurance_training_prs')
        pain_sensitivity_genotype_table = data.get('pain_sensitivity_genotype_table')
        pain_sensitivity_prs = data.get('pain_sensitivity_prs')
        achilles_tendon_injury_genotype_table = data.get('achilles_tendon_injury_genotype_table')
        achilles_tendon_injury_prs = data.get('achilles_tendon_injury_prs')
        muscle_fatigue_and_cramping_genotype_table = data.get('muscle_fatigue_and_cramping_genotype_table')
        muscle_fatigue_and_cramping_prs = data.get('muscle_fatigue_and_cramping_prs')
        aerobic_capacity_genotype_table = data.get('aerobic_capacity_genotype_table')
        aerobic_capacity_prs = data.get('aerobic_capacity_prs')
        response_to_exercise_genotype_table = data.get('response_to_exercise_genotype_table')
        response_to_exercise_prs = data.get('response_to_exercise_prs')
        blood_pressure_genotype_table = data.get('blood_pressure_genotype_table')
        blood_pressure_prs = data.get('blood_pressure_prs')
        wet_vs_dry_earwax_genotype_table = data.get('wet_vs_dry_earwax_genotype_table')
        wet_vs_dry_earwax_prs = data.get('wet_vs_dry_earwax_prs')
        hair_loss_and_baldness_genotype_table = data.get('hair_loss_and_baldness_genotype_table')
        hair_loss_and_baldness_prs = data.get('hair_loss_and_baldness_prs')
        sleep_depth_genotype_table = data.get('sleep_depth_genotype_table')
        sleep_depth_prs = data.get('response_to_exercise_prs')
        warrior_vs_worrier_genotype_table = data.get('warrior_vs_worrier_genotype_table')
        warrior_vs_worrier_prs = data.get('warrior_vs_worrier_prs')
        dental_caries_genotype_table = data.get('dental_caries_genotype_table')
        dental_caries_prs = data.get('dental_caries_prs')

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
            caffeine_metabolism = report_actions.get_caffeine_metabolism(caffeine_prs)
            t2d_risk = report_actions.get_t2d_risk(t2d_prs)
            omega3_and_omega6_level = report_actions.get_omega3_and_omega6_levels(omega_3_prs)
            bitter_taste_perception = report_actions.get_bitter_taste_perception(bitter_taste_perception_prs)
            lactose_intolerance = report_actions.get_lactose_intolerance(lactose_intolerance_prs)
            vitamin_B2 = report_actions.get_vitamin_B2(vitamin_b2_prs)
            vitamin_B12 = report_actions.get_vitamin_B12(vitamin_b12_prs)
            vitamin_C = report_actions.get_vitamin_C(vitamin_c_prs)
            exercise_behavior = report_actions.get_exercise_behavior(exercise_behavior_prs)
            power_and_strength = report_actions.get_power_and_strength(power_and_strength_prs)
            endurance_training = report_actions.get_endurance_training(endurance_training_prs)
            pain_sensitivity = report_actions.get_pain_sensitivity(pain_sensitivity_prs)
            achilles_tendon_injury = report_actions.get_achilles_tendon_injury(achilles_tendon_injury_prs)
            muscle_fatigue_and_cramping = report_actions.get_muscle_fatigue_and_cramping(
                muscle_fatigue_and_cramping_prs)
            aerobic_capacity = report_actions.get_aerobic_capacity(aerobic_capacity_prs)
            blood_pressure_response_to_exercise = report_actions.get_blood_pressure_response_to_exercise(
                blood_pressure_prs)
            bmi_response_to_exercise = report_actions.get_bmi_response_to_exercise(response_to_exercise_prs)

            wet_vs_dry_earwax = report_actions.get_wet_vs_dry_earwax(wet_vs_dry_earwax_prs)
            hair_loss_and_baldness = report_actions.get_hair_loss_and_baldness(hair_loss_and_baldness_prs)
            dental_caries = report_actions.get_dental_caries(dental_caries_prs)
            sleep_depth = report_actions.get_sleep_depth(sleep_depth_prs)
            warrior_vs_worrier = report_actions.get_warrior_vs_worrier(warrior_vs_worrier_prs)

            context = {
                'caffeine_metabolism_recommendation': caffeine_metabolism.recommendation,
                'caffeine_metabolism_result': caffeine_metabolism.result,
                'caffeine_metabolism_interpretation': caffeine_metabolism.interpretation,
                'caffeine_metabolism_image': InlineImage(report, caffeine_metabolism.image.path,
                                                         width=Mm(30)),

                't2d_risk_interpretation': t2d_risk.interpretation,
                't2d_risk_image': InlineImage(report, t2d_risk.image.path,
                                              width=Mm(30)),
                'omega3_and_omega6_level_interpretation': omega3_and_omega6_level.interpretation,
                'omega3_and_omega6_level_result': omega3_and_omega6_level.result,
                'omega3_and_omega6_level_recommendation': omega3_and_omega6_level.recommendation,
                'omega3_and_omega6_level_image': InlineImage(report, omega3_and_omega6_level.image.path,
                                                             width=Mm(30)),
                'lactose_intolerance_interpretation': lactose_intolerance.interpretation,
                'lactose_intolerance_recommendation': lactose_intolerance.recommendation,
                'lactose_intolerance_image': InlineImage(report, lactose_intolerance.image.path,
                                                         width=Mm(30)),
                'bitter_taste_perception_result': bitter_taste_perception.result,
                'bitter_taste_perception_interpretation': bitter_taste_perception.interpretation,
                'bitter_taste_perception_recommendation': bitter_taste_perception.recommendation,
                'bitter_taste_perception_image': InlineImage(report, bitter_taste_perception.image.path,
                                                             width=Mm(30)),
                'vitamin_B2_result': vitamin_B2.result,
                'vitamin_B2_interpretation': vitamin_B2.interpretation,
                'vitamin_B2_recommendation': vitamin_B2.recommendation,
                'vitamin_B2_image': InlineImage(report, vitamin_B2.image.path,
                                                width=Mm(30)),
                'vitamin_B12_result': vitamin_B12.result,
                'vitamin_B12_interpretation': vitamin_B12.interpretation,
                'vitamin_B12_recommendation': vitamin_B12.recommendation,
                'vitamin_B12_image': InlineImage(report, vitamin_B12.image.path,
                                                 width=Mm(30)),

                'vitamin_C_result': vitamin_C.result,
                'vitamin_C_interpretation': vitamin_C.interpretation,
                'vitamin_C_recommendation': vitamin_C.recommendation,
                'vitamin_C_image': InlineImage(report, vitamin_C.image.path,
                                               width=Mm(30)),

                'exercise_behavior_interpretation': exercise_behavior.interpretation,
                'exercise_behavior_result': exercise_behavior.result,

                'power_and_strength_result': power_and_strength.result,
                'power_and_strength_interpretation': power_and_strength.interpretation,
                'power_and_strength_recommendation': power_and_strength.recommendation,
                'power_and_strength_image': InlineImage(report, power_and_strength.image.path, width=Mm(30)),
                'endurance_training_result': endurance_training.result,
                'endurance_training_interpretation': endurance_training.interpretation,
                'endurance_training_recommendation': endurance_training.recommendation,
                'endurance_training_image': InlineImage(report, endurance_training.image.path,
                                                        width=Mm(30)),
                'pain_sensitivity_result': pain_sensitivity.result,
                'pain_sensitivity_interpretation': pain_sensitivity.interpretation,
                'pain_sensitivity_recommendation': pain_sensitivity.recommendation,
                'pain_sensitivity_image': InlineImage(report, pain_sensitivity.image.path,
                                                      width=Mm(30)),
                'achilles_tendon_injury_result': achilles_tendon_injury.result,
                'achilles_tendon_injury_interpretation': achilles_tendon_injury.interpretation,
                'achilles_tendon_injury_recommendation': achilles_tendon_injury.recommendation,
                'achilles_tendon_injury_image': InlineImage(report, achilles_tendon_injury.image.path,
                                                            width=Mm(30)),

                'muscle_fatigue_and_cramping_result': muscle_fatigue_and_cramping.result,
                'muscle_fatigue_and_cramping_interpretation': muscle_fatigue_and_cramping.interpretation,
                'muscle_fatigue_and_cramping_recommendation': muscle_fatigue_and_cramping.recommendation,
                'muscle_fatigue_and_cramping_image': InlineImage(report, muscle_fatigue_and_cramping.image.path,
                                                                 width=Mm(30)),
                'aerobic_capacity_result': aerobic_capacity.result,
                'aerobic_capacity_interpretation': aerobic_capacity.interpretation,
                'aerobic_capacity_recommendation': aerobic_capacity.recommendation,
                'aerobic_capacity_image': InlineImage(report, aerobic_capacity.image.path,
                                                      width=Mm(30)),

                'blood_pressure_response_to_exercise_result': blood_pressure_response_to_exercise.result,
                'blood_pressure_response_to_exercise_interpretation': blood_pressure_response_to_exercise.interpretation,
                'blood_pressure_response_to_exercise_recommendation': blood_pressure_response_to_exercise.recommendation,
                'blood_pressure_response_to_exercise_image': InlineImage(report,
                                                                         blood_pressure_response_to_exercise.image.path,
                                                                         width=Mm(30)),
                'bmi_response_to_exercise_result': bmi_response_to_exercise.result,
                'bmi_response_to_exercise_interpretation': bmi_response_to_exercise.interpretation,
                'bmi_response_to_exercise_recommendation': bmi_response_to_exercise.recommendation,

                'wet_vs_dry_earwax_result': wet_vs_dry_earwax.result,
                'wet_vs_dry_earwax_interpretation': wet_vs_dry_earwax.interpretation,

                'hair_loss_and_baldness_result': hair_loss_and_baldness.result,
                'hair_loss_and_baldness_interpretation': hair_loss_and_baldness.interpretation,

                'sleep_depth_result': sleep_depth.result,
                'sleep_depth_interpretation': sleep_depth.interpretation,

                'dental_caries_result': dental_caries.result,
                'dental_caries_interpretation': dental_caries.interpretation,
                'dental_caries_recommendation': dental_caries.recommendation,

                'warrior_vs_worrier_result': warrior_vs_worrier.result,
                'warrior_vs_worrier_interpretation': warrior_vs_worrier.interpretation,
                'warrior_vs_worrier_recommendation': warrior_vs_worrier.recommendation,
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
                'exercise_behavior_genotype_table': exercise_behavior_genotype_table,
                'power_and_strength_genotype_table': power_and_strength_genotype_table,
                'endurance_training_genotype_table': endurance_training_genotype_table,
                'pain_sensitivity_genotype_table': pain_sensitivity_genotype_table,
                'achilles_tendon_injury_genotype_table': achilles_tendon_injury_genotype_table,
                'muscle_fatigue_and_cramping_genotype_table': muscle_fatigue_and_cramping_genotype_table,
                'aerobic_capacity_genotype_table': aerobic_capacity_genotype_table,
                'response_to_exercise_genotype_table': response_to_exercise_genotype_table,
                'blood_pressure_genotype_table': blood_pressure_genotype_table,
                'wet_vs_dry_earwax_genotype_table': wet_vs_dry_earwax_genotype_table,
                'hair_loss_and_baldness_genotype_table': hair_loss_and_baldness_genotype_table,
                'sleep_depth_genotype_table': sleep_depth_genotype_table,
                'warrior_vs_worrier_genotype_table': warrior_vs_worrier_genotype_table,
                'dental_caries_genotype_table': dental_caries_genotype_table,
            }
            report.render(context)
            report.save("/tovana-root/src/templates/generated_doc.docx")
            report_io = io.BytesIO()
            report.save(report_io)
            report_io.seek(0)
            report = ContentFile(report_io.read())

            nutrition_report = GeneratedReport()
            nutrition_report.report.save(subject.subject_id + ' ' + 'Wellness.docx', report)
            nutrition_report.report_name = subject.subject_id + ' ' + 'Wellness'
            nutrition_report.subject = subject.name
            nutrition_report.created = created_at
            nutrition_report.save()

            request.session['doc_path'] = '"' + nutrition_report.report.path + '"'

        return redirect('report-manager', 'report-builder')
    if action == 'convert_report':
        doc_path = request.session.get('doc_path')
        ret = subprocess.call(['/usr/bin/soffice',
                               '--headless',
                               '--convert-to',
                               'pdf',
                               '--outdir',
                               "/tovana-root/site/public/media/reports/",
                               doc_path])
        if ret:
            return FileResponse(str(ret))
        else:
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
            ## pdf_file_path = "/tovana-root/site/public/media/reports/" + selected_report.report_name + ".pdf"
            pdf_file_path = "/tovana-root/src/templates/generated_doc.pdf"
            return FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')
