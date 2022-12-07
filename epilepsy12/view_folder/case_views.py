from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from epilepsy12.decorator import group_required
from epilepsy12.forms import CaseForm
from epilepsy12.models import HospitalTrust, Site
from ..models import Case
from django.contrib import messages
from ..general_functions import fetch_snomed
from django.core.paginator import Paginator
from django_htmx.http import trigger_client_event, HttpResponseClientRedirect


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

    # get currently selected hospital
    hospital_trust = HospitalTrust.objects.get(pk=hospital_id)

    # get all hospitals which are in the same parent trust
    hospital_children = HospitalTrust.objects.filter(
        ParentName=hospital_trust.ParentName).all()

    if filter_term:
        # filter_term is called if filtering by search box
        if request.user.view_preference == 0:
            # user has requested hospital level view
            all_cases = Case.objects.filter(
                Q(hospital_trusts__OrganisationName__contains=hospital_trust.OrganisationName) &
                Q(site__site_is_primary_centre_of_epilepsy_care=True) &
                Q(first_name__icontains=filter_term) |
                Q(surname__icontains=filter_term) |
                Q(nhs_number__icontains=filter_term)
            ).order_by('surname').all()
        elif request.user.view_preference == 1:
            # user has requested trust level view
            all_cases = Case.objects.filter(
                Q(hospital_trusts__ParentName__contains=hospital_trust.ParentName) &
                Q(site__site_is_primary_centre_of_epilepsy_care=True) &
                Q(first_name__icontains=filter_term) |
                Q(surname__icontains=filter_term) |
                Q(nhs_number__icontains=filter_term)
            ).order_by('surname').all()
        elif request.user.view_preference == 2:
            # user has requested national level view
            all_cases = Case.objects.filter(
                Q(site__site_is_primary_centre_of_epilepsy_care=True) &
                Q(first_name__icontains=filter_term) |
                Q(surname__icontains=filter_term) |
                Q(nhs_number__icontains=filter_term)
            ).order_by('surname').all()

    else:

        """
        Cases are filtered based on user preference (request.user.view_preference), where 0 is hospital level,
        1 is trust level and 2 is national level
        Only RCPCH audit staff have this final option.
        """

        if request.user.view_preference == 2:
            # this is an RCPCH audit team member requesting national view
            filtered_cases = Case.objects.all()
        elif request.user.view_preference == 1:

            # filters all primary Trust level centres, irrespective of if active or inactive
            filtered_cases = Case.objects.filter(
                hospital_trusts__ParentName__contains=hospital_trust.ParentName,
                site__site_is_primary_centre_of_epilepsy_care=True
            )
        else:
            # filters all primary centres at hospital level, irrespective of if active or inactive
            filtered_cases = Case.objects.filter(
                hospital_trusts__OrganisationName__contains=hospital_trust.OrganisationName,
                site__site_is_primary_centre_of_epilepsy_care=True
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
        elif request.htmx.trigger_name == "sort_by_sex_up" or request.GET.get('sort_flag') == "sort_by_sex_up":
            all_cases = filtered_cases.order_by(
                'sex').all()
            sort_flag = "sort_by_sex_up"
        elif request.htmx.trigger_name == "sort_by_sex_down" or request.GET.get('sort_flag') == "sort_by_sex_down":
            all_cases = filtered_cases.order_by(
                '-sex').all()
            sort_flag = "sort_by_sex_down"
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
        (0, f'Hospital View ({hospital_trust.OrganisationName})'),
        (1, f'Trust View ({hospital_trust.ParentName})'),
        (2, 'National View'),
    )

    context = {
        'case_list': case_list,
        'total_cases': case_count,
        'total_registrations': registered_count,
        'sort_flag': sort_flag,
        'hospital_trust': hospital_trust,
        'hospital_children': hospital_children,
        'rcpch_choices': rcpch_choices,
        'hospital_id': hospital_id
    }
    if request.htmx:
        return render(request=request, template_name='epilepsy12/partials/case_table.html', context=context)

    template_name = 'epilepsy12/cases/cases.html'
    return render(request, template_name, context)


# @login_required
def child_hospital_select(request, hospital_id):
    """
    POST call back from hospital_select to allow user to toggle between hospitals in selected trust
    """

    selected_hospital_id = request.POST.get('child_hospital_select')

    # get currently selected hospital
    hospital_trust = HospitalTrust.objects.get(pk=selected_hospital_id)

    # trigger page reload with new hospital
    return HttpResponseClientRedirect(reverse('cases', kwargs={'hospital_id': hospital_trust.pk}))


@login_required
def view_preference(request, hospital_id):
    """
    POST request from Toggle in has rcpch_view_preference.html template
    Users can toggle between national, trust and hospital views.
    Only RCPCH staff can request a national view.
    """
    hospital_trust = HospitalTrust.objects.get(pk=hospital_id)

    rcpch_choices = (
        (0, f'Hospital View ({hospital_trust.OrganisationName})'),
        (1, f'Trust View ({hospital_trust.ParentName})'),
        (2, 'National View'),
    )

    request.user.view_preference = int(request.htmx.trigger_name)
    request.user.save()

    # this is the list of all hospitals in the selected hospital's trust
    hospital_children = HospitalTrust.objects.filter(
        ParentName=hospital_trust.ParentName).all()

    context = {
        'rcpch_choices': rcpch_choices,
        'hospital_trust': hospital_trust,
        'hospital_children': hospital_children
    }

    response = render(
        request, template_name='epilepsy12/partials/cases/view_preference.html', context=context)

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

    if request.user.view_preference == 2:
        # user requesting national view - return all cases in the UK
        total_cases = Case.objects.all()
    elif request.user.view_preference == 1:
        # user requesting trust view - return all cases in the same trust
        total_cases = Case.objects.filter(
            Q(hospital_trusts__ParentName__contains=hospital_trust.ParentName)
        )
    elif request.user.view_preference == 0:
        # user requesting trust view - return all cases in the same hospital
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
def case_submit(request, hospital_id, case_id):
    """
    POST request callback from submit button in case_list partial.
    Toggles case between locked and unlocked
    """
    case = Case.objects.get(pk=case_id)
    case.locked = not case.locked
    case.save()

    return HttpResponseClientRedirect(reverse('cases', kwargs={'hospital_id': hospital_id}))


@login_required
def case_performance_summary(request, case_id):

    case = Case.objects.get(pk=case_id)

    context = {
        'case': case,
        'case_id': case.pk,
        'active_template': 'case_performance_summary',
        'audit_progress': case.registration.audit_progress,
    }

    template = 'epilepsy12/case_performance_summary.html'

    response = render(request=request, template_name=template, context=context)

    return response


"""
Case function based views - class based views not chosen as need to accept hospital_id also in URL
"""


@login_required
@permission_required('epilepsy12.add_case')
def create_case(request, hospital_id):
    """
    Django function based - returns django form to create a new case, or saves a new case if a
    POST request. The only instance where htmx not used.
    """
    hospital_trust = HospitalTrust.objects.filter(
        OrganisationID=hospital_id).get()
    form = CaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_at = datetime.now()
            hospital = HospitalTrust.objects.get(pk=hospital_id)
            # save the new child
            obj.save()
            # allocate the child to the hospital supplied as primary E12 centre
            Site.objects.create(
                site_is_actively_involved_in_epilepsy_care=True,
                site_is_primary_centre_of_epilepsy_care=True,
                hospital_trust=hospital,
                case=obj
            )
            messages.success(request, "You successfully created the case")
        else:
            messages.error(request, "Case not created")
            return redirect('cases', hospital_id=hospital_id)

    context = {
        "hospital_id": hospital_id,
        "hospital_trust": hospital_trust,
        "form": form
    }
    return render(request=request, template_name='epilepsy12/cases/case.html', context=context)


@login_required
@group_required('epilepsy12_audit_team_edit_access', 'epilepsy12_audit_team_full_access', 'trust_audit_team_edit_access', 'trust_audit_team_full_access')
def update_case(request, hospital_id, case_id):
    """
    Django function based view. Receives POST request to update view or delete
    """
    case = get_object_or_404(Case, pk=case_id)
    form = CaseForm(instance=case)

    hospital_trust = HospitalTrust.objects.filter(
        OrganisationID=hospital_id).get()

    if request.method == "POST":
        if ('delete') in request.POST:
            case.delete()
            return redirect('cases', hospital_id=hospital_id)
        form = CaseForm(request.POST, instance=case)
        if form.is_valid:
            obj = form.save()
            if (case.locked != obj.locked):
                # locked status has changed
                if (form.locked):
                    obj.locked_by = request.user
                    obj.locked_at = datetime.now()
                else:
                    obj.locked_by = None
                    obj.locked_at = None
            obj.updated_at = timezone.now(),
            obj.updated_by = request.user
            obj.save()
            messages.success(
                request, "You successfully updated the child's details")
            return redirect('cases', hospital_id=hospital_id)

    context = {
        "hospital_id": hospital_id,
        "hospital_trust": hospital_trust,
        "form": form,
        'case': case
    }

    return render(request=request, template_name='epilepsy12/cases/case.html', context=context)


@login_required
@group_required('epilepsy12_audit_team_full_access', 'trust_audit_team_full_access')
def delete_case(request, hospital_id, case_id):
    case = get_object_or_404(Case, id=case_id)
    case.delete()
    return redirect('cases', hospital_id=hospital_id)


@login_required
def opt_out(request, hospital_id, case_id):
    """
    This child has opted out of Epilepsy12
    Their unique E12 ID will be retained but all associated fields will be set to None, and associated records deleted except their 
    leading trust will be retained but set to inactive.
    """

    # hospital_trust = HospitalTrust.objects.get(pk=hospital_id)
    case = Case.objects.get(pk=case_id)
    case.nhs_number = None
    case.first_name = None
    case.surname = None
    case.sex = None
    case.date_of_birth = None
    case.postcode = None
    case.ethnicity = None
    case.locked = True

    case.save()

    # delete all related records - this should cascade to all tables
    case.registration.delete()

    # delete all related sites except the primary centre of care, which becomes inactive
    all_sites = case.site.all()
    for site in all_sites:
        if site.site_is_primary_centre_of_epilepsy_care:
            site.site_is_actively_involved_in_epilepsy_care = False
            site.save()
        else:
            Site.objects.get(pk=site.pk).delete()

    return HttpResponseClientRedirect(reverse('cases', kwargs={'hospital_id': hospital_id}))
