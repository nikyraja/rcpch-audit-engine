from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from epilepsy12.decorator import group_required
from epilepsy12.forms import CaseForm
from epilepsy12.models import HospitalTrust, Epilepsy12User
from ..models import Case
from django.contrib import messages
from ..general_functions import fetch_snomed
from django.core.paginator import Paginator
from django_htmx.http import trigger_client_event


@login_required
def case_list(request, hospital_id):
    """
    Returns a list of all children registered under the user's service.
    Path is protected to those logged in only
    Params:
    request.user

    If the user is a clinician / centre lead, only the children under their care are seen (whether registered or not)
    If the user is an audit administrator, they have can view all cases in the audit, but cannot edit
    If the user is a superuser, they can view and edit all cases in the audit (but with great power comes great responsibility)

    #TODO #32 Audit trail of all viewing or touching the database

    """

    sort_flag = None

    filter_term = request.GET.get('filtered_case_list')

    hospital_trust = HospitalTrust.objects.get(pk=hospital_id)

    if filter_term:
        all_cases = Case.objects.filter(
            Q(hospital_trusts__OrganisationName__contains=hospital_trust.OrganisationName) &
            Q(first_name__icontains=filter_term) |
            Q(surname__icontains=filter_term) |
            Q(nhs_number__icontains=filter_term)
        ).order_by('surname').all()
    else:

        # filter cases by hospital trust if logged in user is not RCPCH audit staff
        # RCPCH Staff members that are also clinicians can choose which view
        if request.user.is_rcpch_audit_team_member and request.user.has_rcpch_view_preference:
            filtered_cases = Case.objects.all()
        else:
            filtered_cases = Case.objects.filter(
                hospital_trusts__OrganisationName__contains=hospital_trust.OrganisationName
            )

        if request.htmx.trigger_name == "sort_by_imd_up" or request.GET.get('sort_flag') == "sort_by_imd_up":
            # this is to sort on IMD
            all_cases = filtered_cases.order_by(
                'index_of_multiple_deprivation_quintile').all()
            sort_flag = "sort_by_imd_up"
        elif request.htmx.trigger_name == "sort_by_imd_down" or request.GET.get('sort_flag') == "sort_by_imd_down":
            all_cases = filtered_cases.order_by(
                '-index_of_multiple_deprivation_quintile').all()
            sort_flag = "sort_by_imd_down"
        elif request.htmx.trigger_name == "sort_by_nhs_number_up" or request.GET.get('sort_flag') == "sort_by_nhs_number_up":
            all_cases = filtered_cases.order_by(
                'nhs_number').all()
            sort_flag = "sort_by_nhs_number_up"
        elif request.htmx.trigger_name == "sort_by_nhs_number_down" or request.GET.get('sort_flag') == "sort_by_nhs_number_down":
            all_cases = filtered_cases.order_by(
                '-nhs_number').all()
            sort_flag = "sort_by_nhs_number_down"
        elif request.htmx.trigger_name == "sort_by_ethnicity_up" or request.GET.get('sort_flag') == "sort_by_ethnicity_up":
            all_cases = filtered_cases.order_by(
                'ethnicity').all()
            sort_flag = "sort_by_ethnicity_up"
        elif request.htmx.trigger_name == "sort_by_ethnicity_down" or request.GET.get('sort_flag') == "sort_by_ethnicity_down":
            all_cases = filtered_cases.order_by(
                '-ethnicity').all()
            sort_flag = "sort_by_ethnicity_down"
        elif request.htmx.trigger_name == "sort_by_gender_up" or request.GET.get('sort_flag') == "sort_by_gender_up":
            all_cases = filtered_cases.order_by(
                'gender').all()
            sort_flag = "sort_by_gender_up"
        elif request.htmx.trigger_name == "sort_by_gender_down" or request.GET.get('sort_flag') == "sort_by_gender_down":
            all_cases = filtered_cases.order_by(
                '-sex').all()
            sort_flag = "sort_by_gender_down"
        elif request.htmx.trigger_name == "sort_by_name_up" or request.GET.get('sort_flag') == "sort_by_name_up":
            all_cases = filtered_cases.order_by(
                'surname').all()
            sort_flag = "sort_by_name_up"
        elif request.htmx.trigger_name == "sort_by_name_down" or request.GET.get('sort_flag') == "sort_by_name_down":
            all_cases = filtered_cases.order_by(
                '-surname').all()
            sort_flag = "sort_by_name_down"
        elif request.htmx.trigger_name == "sort_by_id_up" or request.GET.get('sort_flag') == "sort_by_id_up":
            all_cases = filtered_cases.order_by(
                'id').all()
            sort_flag = "sort_by_id_up"
        elif request.htmx.trigger_name == "sort_by_id_down" or request.GET.get('sort_flag') == "sort_by_id_down":
            all_cases = filtered_cases.order_by(
                '-id').all()
            sort_flag = "sort_by_id_down"
        else:
            all_cases = filtered_cases.order_by('surname').all()

    registered_cases = all_cases.filter(
        ~Q(registration__isnull=True),
    ).all()


#     fetch_snomed(365456003, 'descendentSelfOf')

    paginator = Paginator(all_cases, 10)
    page_number = request.GET.get('page', 1)
    case_list = paginator.page(page_number)

    case_count = all_cases.count()
    registered_count = registered_cases.count()

    rcpch_choices = (
        (0, 'All UK Children'),
        (1, f'{hospital_trust.OrganisationName} Cohort')
    )
    if request.user.has_rcpch_view_preference:
        rcpch_preference = rcpch_choices[0][0]
    else:
        rcpch_preference = rcpch_choices[1][0]

    context = {
        'case_list': case_list,
        'total_cases': case_count,
        'total_registrations': registered_count,
        'sort_flag': sort_flag,
        'hospital_trust': hospital_trust,
        'rcpch_choices': rcpch_choices,
        'rcpch_preference': rcpch_preference
    }
    if request.htmx:
        return render(request=request, template_name='epilepsy12/partials/case_table.html', context=context)

    template_name = 'epilepsy12/cases/cases.html'
    return render(request, template_name, context)


@login_required
@group_required('epilepsy12_audit_team_edit_access', 'epilepsy12_audit_team_full_access', 'trust_audit_team_edit_access', 'trust_audit_team_full_access')
def create_case(request):
    form = CaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_at = datetime.now()
            obj.save()
            messages.success(request, "You successfully created the case")
            return redirect('cases')

    context = {
        "form": form
    }
    return render(request=request, template_name='epilepsy12/cases/case.html', context=context)


@login_required
def has_rcpch_view_preference(request, hospital_id):
    """
    Toggle visible only to clinicians who are also RCPCH audit team members
    Can toggle between their own trust and RCPCH view
    """
    hospital_trust = HospitalTrust.objects.get(pk=hospital_id)

    rcpch_choices = (
        (0, 'All UK Children'),
        (1, f'{hospital_trust.OrganisationName} Cohort')
    )

    if (int(request.htmx.trigger_name) == 1):

        request.user.has_rcpch_view_preference = False
        request.user.save()
        rcpch_preference = rcpch_choices[1][0]

    elif (int(request.htmx.trigger_name) == 0):
        request.user.has_rcpch_view_preference = True
        request.user.save()

        rcpch_preference = rcpch_choices[0][0]

    context = {
        'rcpch_choices': rcpch_choices,
        'rcpch_preference': rcpch_preference,
        'hospital_trust': hospital_trust
    }

    response = render(
        request, template_name='epilepsy12/partials/cases/has_rcpch_view_preference.html', context=context)

    # trigger a GET request to rerender the case list
    trigger_client_event(
        response=response,
        name="case_list",
        params={})  # reloads the form to show the updated cases

    # trigger a GET request to rerender the case list statistics
    trigger_client_event(
        response=response,
        name="case_statistics",
        params={})  # reloads the form to show the updated cases

    return response


def case_statistics(request, hospital_id):
    """
    GET request from cases template to update stats on toggle between RCPCH view and hospital view
    """

    hospital_trust = HospitalTrust.objects.get(pk=hospital_id)

    if request.user.has_rcpch_view_preference:
        total_cases = Case.objects.all()
    else:
        total_cases = Case.objects.filter(
            Q(hospital_trusts__OrganisationName__contains=hospital_trust.OrganisationName)
        )

    registered_cases = total_cases.filter(
        ~Q(registration__isnull=True),
    ).all()

    context = {
        'total_cases': total_cases.count(),
        'total_registrations': registered_cases.count(),
        'hospital_trust': hospital_trust
    }

    response = render(
        request, template_name='epilepsy12/partials/cases/case_statistics.html', context=context)

    return response


@login_required
@group_required('epilepsy12_audit_team_edit_access', 'epilepsy12_audit_team_full_access', 'trust_audit_team_edit_access', 'trust_audit_team_full_access')
def update_case(request, id):
    case = get_object_or_404(Case, id=id)
    form = CaseForm(instance=case)

    if request.method == "POST":
        if ('delete') in request.POST:
            case.delete()
            return redirect('cases')
        form = CaseForm(request.POST, instance=case)
        if form.is_valid:
            obj = form.save()
            if (case.locked != form.locked):
                # locked status has changed
                if (form.locked):
                    obj.locked_by = request.user
                    obj.locked_at = datetime.now()
                else:
                    obj.locked_by = None
                    obj.locked_at = None
            obj.save()
            messages.success(
                request, "You successfully updated the child's details")
            return redirect('cases')

    context = {
        "form": form
    }

    return render(request=request, template_name='epilepsy12/cases/case.html', context=context)


@login_required
@group_required('epilepsy12_audit_team_full_access', 'trust_audit_team_full_access')
def delete_case(request, id):
    case = get_object_or_404(Case, id=id)
    case.delete()
    return redirect('cases')
