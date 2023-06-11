from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Goal, TempMoment
from .models import ProudMoment
from .models import BestMoment
from .forms import MomentsForm, TempSaveForm
from .gobal_vars import current_version
from .gobal_vars import versions


def landing_page(request):
    return render(request, 'landing_page.html')

def history_page(request):
    context = {

    }
    display_version = {}
    # too many db calls change it later
    for version in range(current_version -1, -1, -1):
        goals_exist =  Goal.objects.filter(user_name='rajiv', best_version=versions[version]).exists()
        if goals_exist:
            past_version_goal = Goal.objects.filter(user_name='rajiv', best_version=versions[version]).latest('id')
        else:
            past_version_goal = ''
        previous_proud_moments = ProudMoment.objects.filter(user_name='rajiv', best_version=versions[version])
        previous_best_moments  = BestMoment.objects.filter(user_name='rajiv', best_version=versions[version])
        version_content= {'goals' : past_version_goal}
        version_content.update({'p_m':previous_proud_moments, 'b_m':previous_best_moments})

        display_version[versions[version]] = version_content

    context['display_version'] = display_version


    return render(request,'history_page.html', context)

def current_page(request):
    context = {
        'current_decade': versions[current_version]
    }
    form1 = MomentsForm()
    form2 = TempSaveForm()

    if request.method == 'POST':
        form1 = MomentsForm(request.POST)
        form2 = TempSaveForm(request.POST)
        # if actual moments save it in db for current_version
        if form1.is_valid():
            user_proud_moments = form1.cleaned_data['proud_moments']
            user_best_moments = form1.cleaned_data['best_moments']

            print("userr pm "+user_proud_moments)
            print("user bm "+ user_best_moments)

            # to save current moments, show modal
            if user_proud_moments:
                proud_moments_exists = ProudMoment.objects.filter(user_name='rajiv', best_version=versions[current_version])
                # save pm only once
                if not proud_moments_exists:

                    proud_moments = user_proud_moments.splitlines()
                    for moment in proud_moments:
                        # dont submit id the user version is already submitted --- actual version here
                        # issue
                        proud_moment_instance = ProudMoment(user_name='rajiv', best_version=versions[current_version], proud_moment_text=moment)
                        proud_moment_instance.save()
            if user_best_moments:
                best_moments_exists = BestMoment.objects.filter(user_name='rajiv', best_version=versions[current_version])
                # save bm only once
                if not best_moments_exists:
                    best_moments = user_best_moments.splitlines()
                    for moment in best_moments:
                        # dont submit id the user version is already submitted
                        best_moment_instance = BestMoment(user_name='rajiv', best_version=versions[current_version], best_moment_text=moment)
                        best_moment_instance.save()
            context['show_modal'] = True
            # update best_version & clear temp_moment data in db  --- do it manually for now--

        # this is daily use -- to not forget some imp moments
        # to store temp just to not forget on end day of version --- save it in temp db
        if form2.is_valid():
            temp_moments = form2.cleaned_data['temp_moments']
            print("user don't forget moments "+temp_moments)
            if temp_moments:
                temp_moments = temp_moments.splitlines()
                for moment in temp_moments:
                    temp_moment_exists = TempMoment.objects.filter(temp_moment = moment)
                    if not temp_moment_exists:
                        temp_moment_instance = TempMoment(temp_moment = moment)
                        temp_moment_instance.save()


    else:
        context['show_modal'] = False

    context['form1'] = form1
    context['form2'] = form2




    # goals part
    user_current_goal = request.GET.get('textbox')

    # to save current goal and display
    if user_current_goal:
        context['user_current_goal'] = user_current_goal.split(' ')
        goal_instance = Goal(goal_text=user_current_goal, user_name='rajiv', best_version=versions[current_version])
        goal_instance.save()
        print("saving user_current_goal " + user_current_goal)
    else:
        # if goal is already der display that
        if Goal.objects.filter(user_name='rajiv', best_version=versions[current_version]).exists():
            goal = Goal.objects.filter(user_name='rajiv', best_version=versions[current_version]).latest('id')
            context['user_current_goal'] = goal.goal_text.split(' ')


    # to retrive privous moments
    previous_proud_moments = ProudMoment.objects.filter(user_name='rajiv', best_version=versions[current_version-1])
    previous_best_moments  = BestMoment.objects.filter(user_name='rajiv', best_version=versions[current_version-1])
    if previous_proud_moments:
        context['previous_proud_moments']  = previous_proud_moments
    if previous_best_moments:
        context['previous_best_moments']  = previous_best_moments

    return render(request, 'current_page.html', context)
