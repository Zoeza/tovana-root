from django.shortcuts import render


# Create your views here.
def report_manager(request, action):
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
