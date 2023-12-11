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

    try:
        departments_list = Department.objects.all()
    except Department.DoesNotExist:
        raise Http404("No departments")

    try:
        subjects_list = Subject.objects.all()
    except Subject.DoesNotExist:
        raise Http404("No subjects")

    try:
        reports_list = GeneratedReport.objects.all()
    except GeneratedReport.DoesNotExist:
        raise Http404("No subjects")

    direction = request.session.get('language')
    nav_side = 'report builder'

    if action == 'report-builder':
        url = direction + "/report_builder/reports/list.html"

        context = {
            'reports_list': reports_list,
            'nav_side': nav_side,
        }
        return render(request, url, context)
