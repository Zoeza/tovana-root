from django.shortcuts import render
from .models import Subject, Template, Department, GeneratedReport
from django.http import Http404


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
            'nav_side': nav_side,
        }
        return render(request, url, context)
