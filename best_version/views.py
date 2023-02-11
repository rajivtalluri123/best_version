from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Goal
from .models import ProudMoment
from .models import BestMoment
from .gobal_vars import current_version
from .gobal_vars import versions


def landing_page(request):
    current_year = datetime.datetime.now().year
    context = {
        'current_year': current_year,
        'dynamic_content': 'This is some dynamic content'
    }
    return render(request, 'landing_page.html', context)


def current_page(request):
    context = {
        'current_decade': versions[current_version]
    }

    user_current_goal = request.GET.get('textbox')
    user_proud_moments = request.GET.get('user_proud_moments')
    user_best_moments = request.GET.get('user_best_moments')

    # to save current goal and display
    if user_current_goal:
        context['user_current_goal'] = user_current_goal.split(' ')
        goal_instance = Goal(goal_text=user_current_goal, user_name='rajiv', best_version='23.2.1')
        goal_instance.save()
        print("saving user_current_goal " + user_current_goal)
    else:
        # if goal is already der display that
        goal = Goal.objects.filter(user_name='rajiv', best_version='23.2.1').latest('id')
        if goal:
            context['user_current_goal'] = goal.goal_text.split(' ')

    # to save current moments, show modal
    if user_proud_moments:
        proud_moments = user_proud_moments.splitlines()
        print(proud_moments)
        for moment in proud_moments:
            proud_moment_instance = ProudMoment(user_name='rajiv', best_version='10.10.10', proud_moment_text=moment)
            proud_moment_instance.save()
    if user_best_moments:
        best_moments = user_best_moments.splitlines()
        print(best_moments)
        for moment in best_moments:
            best_moment_instance = BestMoment(user_name='rajiv', best_version='10.10.10', best_moment_text=moment)
            best_moment_instance.save()
    if user_best_moments or user_proud_moments:
        # update best_version
        context['show_modal'] = True
    else:
        context['show_modal'] = False

    # to retrive privous moments
    previous_proud_moments = ProudMoment.objects.filter(user_name='rajiv', best_version='23.1.3')
    previous_best_moments  = BestMoment.objects.filter(user_name='rajiv', best_version='23.1.3')
    if previous_proud_moments:
        context['previous_proud_moments']  = previous_proud_moments
    if previous_best_moments:
        context['previous_best_moments']  = previous_best_moments

    return render(request, 'current_page.html', context)
