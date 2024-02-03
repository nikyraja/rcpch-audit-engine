"""

## Create Tests

    [x] Assert an Audit Centre Lead Clinician can create users inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can create users nationally, inside own Trust, and outside  - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can create users nationally, inside own Trust, and outside  - response.status_code == HTTPStatus.OK

    [x] Assert an Audit Centre Administrator CANNOT create users - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an audit centre clinician CANNOT create users - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT create users outside own Trust - response.status_code == HTTPStatus.FORBIDDEN


    [x] Assert an Audit Centre Administrator can create patients inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Clinician can create patients inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can create patients inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can create patients  inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can create patients  inside own Trust  - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can create patients  outside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can create patients  outside own Trust - response.status_code == HTTPStatus.OK

    [x] Assert an Audit Centre Administrator CANNOT create patients outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an audit centre clinician CANNOT create patients outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT create patients outside own Trust - response.status_code == HTTPStatus.FORBIDDEN


    [ ] Assert an Audit Centre Clinician can create patient records inside own Trust - response.status_code == HTTPStatus.OK
    [ ] Assert an Audit Centre Lead Clinician can create patient records inside own Trust - response.status_code == HTTPStatus.OK
    [ ] Assert RCPCH Audit Team can create patient records nationally, inside own Trust, and outside  - response.status_code == HTTPStatus.OK
    [ ] Assert Clinical Audit Team can create patient records nationally, inside own Trust, and outside  - response.status_code == HTTPStatus.OK

    [ ] Assert an Audit Centre Administrator CANNOT create patient records - response.status_code == HTTPStatus.FORBIDDEN
    [ ] Assert an audit centre clinician CANNOT create patient records outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [ ] Assert an Audit Centre Lead Clinician CANNOT create patient records outside own Trust - response.status_code == HTTPStatus.FORBIDDEN



# Episode

    [x] Assert an Audit Centre Clinician can 'add_episode' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can 'add_episode' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_episode' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_episode' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_episode' inside different Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_episode' inside different Trust - response.status_code == HTTPStatus.OK
    
    [x] Assert an Audit Centre Administrator CANNOT 'add_episode' - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician CANNOT 'add_episode' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT 'add_episode' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN

# Comorbidity

    [x] Assert an Audit Centre Clinician can 'add_comorbidity' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can 'add_comorbidity' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_comorbidity' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_comorbidity' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_comorbidity' inside different Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_comorbidity' inside different Trust - response.status_code == HTTPStatus.OK
    
    [x] Assert an Audit Centre Administrator CANNOT 'add_comorbidity' - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician CANNOT 'add_comorbidity' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT 'add_comorbidity' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN

# Syndrome

    [x] Assert an Audit Centre Clinician can 'add_syndrome' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can 'add_syndrome' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_syndrome' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_syndrome' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_syndrome' inside different Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_syndrome' inside different Trust - response.status_code == HTTPStatus.OK
    
    [x] Assert an Audit Centre Administrator CANNOT 'add_syndrome' - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician CANNOT 'add_syndrome' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT 'add_syndrome' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN


# Antiepilepsy Medicine

    [x] Assert an Audit Centre Clinician can 'add_antiepilepsy_medicine' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert an Audit Centre Lead Clinician can 'add_antiepilepsy_medicine' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_antiepilepsy_medicine' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_antiepilepsy_medicine' inside own Trust - response.status_code == HTTPStatus.OK
    [x] Assert RCPCH Audit Team can 'add_antiepilepsy_medicine' inside different Trust - response.status_code == HTTPStatus.OK
    [x] Assert Clinical Audit Team can 'add_antiepilepsy_medicine' inside different Trust - response.status_code == HTTPStatus.OK
    
    [x] Assert an Audit Centre Administrator CANNOT 'add_antiepilepsy_medicine' - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Clinician CANNOT 'add_antiepilepsy_medicine' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
    [x] Assert an Audit Centre Lead Clinician CANNOT 'add_antiepilepsy_medicine' outside own Trust - response.status_code == HTTPStatus.FORBIDDEN
"""

# python imports
import pytest
from http import HTTPStatus
from datetime import date

# django imports
from django.urls import reverse

# E12 Imports
from epilepsy12.tests.UserDataClasses import (
    test_user_audit_centre_administrator_data,
    test_user_audit_centre_clinician_data,
    test_user_audit_centre_lead_clinician_data,
    test_user_clinicial_audit_team_data,
    test_user_rcpch_audit_team_data,
)
from epilepsy12.models import (
    Epilepsy12User,
    Organisation,
    Case,
)
from epilepsy12.tests.view_tests.permissions_tests.perm_tests_utils import (
    twofactor_signin,
)


@pytest.mark.django_db
def test_user_create_same_org_success(
    client,
    seed_groups_fixture,
    seed_users_fixture,
    seed_cases_fixture,
):
    """Integration test checking functionality of view and form.

    Simulating different E12 users with different roles attempting to create Users inside own trust.
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ods_code="RP401",
        trust__ods_code="RP4",
    )

    TEMP_CREATED_USER_FIRST_NAME = "TEMP_CREATED_USER_FIRST_NAME"

    selected_users = [
        test_user_audit_centre_lead_clinician_data.role_str,
        test_user_rcpch_audit_team_data.role_str,
        test_user_clinicial_audit_team_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        url = reverse(
            "create_epilepsy12_user",
            kwargs={
                "organisation_id": TEST_USER_ORGANISATION.id,
                "user_type": "organisation-staff",
                "epilepsy12_user_id": test_user.id,
            },
        )

        response = client.get(url)

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested `{url}` of {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()}. Expected 200 response status code, received {response.status_code}"

        data = {
            "title": 1,
            "email": f"{test_user.first_name}@test.com",
            "role": 1,
            "organisation_employer": TEST_USER_ORGANISATION.id,
            "first_name": TEMP_CREATED_USER_FIRST_NAME,
            "surname": "User",
            "is_rcpch_audit_team_member": False,
            "is_rcpch_staff": False,
            "email_confirmed": True,
        }

        response = client.post(url, data=data)

        # This is valid form data, should redirect
        assert (
            response.status_code == HTTPStatus.FOUND
        ), f"Valid E12User form data POSTed by {test_user}, expected status_code 302, received {response.status_code}"

    assert (
        Epilepsy12User.objects.filter(first_name=TEMP_CREATED_USER_FIRST_NAME).count()
        == 3
    ), f"Logged in as 3 different people and created an e12 user with first_name = {TEMP_CREATED_USER_FIRST_NAME}. Should be 3 matches in db for this filter."


@pytest.mark.django_db
def test_user_create_diff_org_success(
    client,
):
    """Integration test checking functionality of view and form.

    RCPCH Audit Team and Clinical Audit Team roles should be able to create user in different trust.
    """

    # set up constants

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    TEMP_CREATED_USER_FIRST_NAME = "TEMP_CREATED_USER_FIRST_NAME"

    selected_users = [
        test_user_rcpch_audit_team_data.role_str,
        test_user_clinicial_audit_team_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        url = reverse(
            "create_epilepsy12_user",
            kwargs={
                "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
                "user_type": "organisation-staff",
                "epilepsy12_user_id": test_user.id,
            },
        )

        data = {
            "title": 1,
            "email": f"{test_user.first_name}@test.com",
            "role": 1,
            "organisation_employer": DIFF_TRUST_DIFF_ORGANISATION.id,
            "first_name": TEMP_CREATED_USER_FIRST_NAME,
            "surname": "User",
            "is_rcpch_audit_team_member": True,
            "is_rcpch_staff": False,
            "email_confirmed": True,
        }

        response = client.post(url, data=data)

        # This is valid form data, should redirect
        assert (
            response.status_code == HTTPStatus.FOUND
        ), f"Valid E12User form data POSTed by {test_user}, expected status_code 302, received {response.status_code}"

    assert (
        Epilepsy12User.objects.filter(first_name=TEMP_CREATED_USER_FIRST_NAME).count()
        == 2
    ), f"Logged in as 2 different people and created an e12 user with first_name = {TEMP_CREATED_USER_FIRST_NAME}. Should be 2 matches in db for this filter."


@pytest.mark.django_db
def test_user_creation_forbidden(
    client,
):
    """Integration test checking functionality of view and form.

    Simulating unpermitted E12 users attempting to create Users inside own trust.

    Additionally, AUDIT_CENTRE_LEAD_CLINICIAN role CANNOT create user in different trust.
    """

    # set up constants

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    TEMP_CREATED_USER_FIRST_NAME = "TEMP_CREATED_USER_FIRST_NAME"

    selected_users = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        url = reverse(
            "create_epilepsy12_user",
            kwargs={
                "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
                "user_type": "organisation-staff",
                "epilepsy12_user_id": test_user.id,
            },
        )

        response = client.get(url)

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested `{url}` of {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()}. Expected {HTTPStatus.FORBIDDEN} response status code, received {response.status_code}"

        data = {
            "title": 1,
            "email": f"{test_user.first_name}@test.com",
            "role": 1,
            "organisation_employer": DIFF_TRUST_DIFF_ORGANISATION.id,
            "first_name": TEMP_CREATED_USER_FIRST_NAME,
            "surname": "User",
            "is_rcpch_audit_team_member": True,
            "is_rcpch_staff": False,
            "email_confirmed": True,
        }

        response = client.post(url, data=data)

        # This is valid form data, should redirect
        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"Unpermitted E12User {test_user} attempted to create an E12User. expected status_code {HTTPStatus.FORBIDDEN}, received {response.status_code}"

    assert (
        Epilepsy12User.objects.filter(first_name=TEMP_CREATED_USER_FIRST_NAME).count()
        == 0
    ), f"Logged in as 3 different unpermitted Users and attempted to create an e12 user with first_name = {TEMP_CREATED_USER_FIRST_NAME}. Should be 0 matches in db for this filter."


@pytest.mark.django_db
def test_patient_create_success(
    client,
):
    """Integration test checking functionality of view and form.

    Simulating different E12 users with different roles attempting to create Patients inside own trust.
    """

    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ods_code="RP401",
        trust__ods_code="RP4",
    )

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    TEST_FIRST_NAME = "TEST_FIRST_NAME"

    selected_users = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
        test_user_rcpch_audit_team_data.role_str,
        test_user_clinicial_audit_team_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        url = reverse(
            "create_case",
            kwargs={
                "organisation_id": TEST_USER_ORGANISATION.id,
            },
        )

        response = client.get(url)

        assert (
            response.status_code == HTTPStatus.OK
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested `{url}` of {TEST_USER_ORGANISATION}. Has groups: {test_user.groups.all()}. Expected 200 response status code, received {response.status_code}"

        data = {
            "first_name": TEST_FIRST_NAME,
            "surname": "Chandran",
            "date_of_birth": date(2023, 6, 15),
            "sex": "1",
            "nhs_number": "400 0000 012",
            "postcode": "SW1A 1AA",
            "ethnicity": "N",
        }

        response = client.post(url, data=data)

        # This is valid form data, should redirect
        assert (
            response.status_code == HTTPStatus.FOUND
        ), f"Valid Case form data POSTed by {test_user}, expected status_code {HTTPStatus.FOUND}, received {response.status_code}"

        assert Case.objects.filter(
            first_name=TEST_FIRST_NAME
        ).exists(), f"Logged in as {test_user} and created Case at {url}. Created Case not found in db."

        # Remove Case for next user
        Case.objects.filter(first_name=TEST_FIRST_NAME).delete()

        # Additionally RCPCH_AUDIT_TEAM and CLINICAL_AUDIT_TEAM can create Case in different Trust
        if test_user.first_name in [
            test_user_rcpch_audit_team_data.role_str,
            test_user_clinicial_audit_team_data.role_str,
        ]:
            url = reverse(
                "create_case",
                kwargs={
                    "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
                },
            )

            response = client.get(url)

            assert (
                response.status_code == HTTPStatus.OK
            ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested `{url}` of {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()}. Expected 200 response status code, received {response.status_code}"

            data = {
                "first_name": TEST_FIRST_NAME,
                "surname": "Chandran",
                "date_of_birth": date(2023, 6, 15),
                "sex": "1",
                "nhs_number": "400 0000 012",
                "postcode": "SW1A 1AA",
                "ethnicity": "N",
            }

            response = client.post(url, data=data)

            # This is valid form data, should redirect
            assert (
                response.status_code == HTTPStatus.FOUND
            ), f"Valid Case form data POSTed by {test_user}, expected status_code 302, received {response.status_code}"

            assert Case.objects.filter(
                first_name=TEST_FIRST_NAME
            ).exists(), f"Logged in as {test_user} and created Case at {url}. Created Case not found in db."

            # Remove Case for next user
            Case.objects.filter(first_name=TEST_FIRST_NAME).delete()


@pytest.mark.django_db
def test_patient_creation_forbidden(
    client,
):
    """Integration test checking functionality of view and form.

    Simulating unpermitted E12 Users attempting to create patients.

    Additionally, AUDIT_CENTRE_LEAD_CLINICIAN role only NOT ALLOWED to create patient in different trust.
    """

    # set up constants

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    TEST_FIRST_NAME = "TEST_FIRST_NAME"

    selected_users = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        url = reverse(
            "create_case",
            kwargs={
                "organisation_id": DIFF_TRUST_DIFF_ORGANISATION.id,
            },
        )

        response = client.get(url)

        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"{test_user.first_name} (from {test_user.organisation_employer}) requested `{url}` of {DIFF_TRUST_DIFF_ORGANISATION}. Has groups: {test_user.groups.all()}. Expected {HTTPStatus.FORBIDDEN} status code, received {response.status_code}"

        data = {
            "first_name": TEST_FIRST_NAME,
            "surname": "Chandran",
            "date_of_birth": date(2023, 6, 15),
            "sex": "1",
            "nhs_number": "400 0000 012",
            "postcode": "SW1A 1AA",
            "ethnicity": "N",
        }

        response = client.post(url, data=data)

        # This is valid form data but should be forbidden
        assert (
            response.status_code == HTTPStatus.FORBIDDEN
        ), f"Valid Case form data POSTed by unpermitted {test_user}, expected status_code {HTTPStatus.FORBIDDEN}, received {response.status_code}"

        assert not Case.objects.filter(
            first_name=TEST_FIRST_NAME
        ).exists(), f"Logged in as {test_user} and attempted to Case at {url}. Unpermitted so Case should not be created."


@pytest.mark.django_db
def test_add_episode_comorbidity_syndrome_aem_success(client):
    """
    Simulating different permitted E12 Roles request.POSTing to the following htmx urls:

        - `add_episode`
        - `add_comorbidity`
        - `add_syndrome`
        - `add_antiepilepsy_medicine`

    Additionally, RCPCH_AUDIT_TEAM and CLINICAL_AUDIT_TEAM can add Episode in different Trust.
    """
    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ods_code="RP401",
        trust__ods_code="RP4",
    )

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.name}"
    )

    URLS = [
        "add_episode",
        "add_comorbidity",
        "add_syndrome",
        "add_antiepilepsy_medicine",
    ]

    selected_users = [
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
        test_user_rcpch_audit_team_data.role_str,
        test_user_clinicial_audit_team_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        # OTP ENABLE
        twofactor_signin(client, test_user)

        for url in URLS:
            if url == "add_antiepilepsy_medicine":
                kwargs = {
                    "management_id": CASE_FROM_SAME_ORG.registration.management.id,
                    "is_rescue_medicine": "is_rescue_medicine",
                }
            else:
                kwargs = {
                    "multiaxial_diagnosis_id": CASE_FROM_SAME_ORG.registration.multiaxialdiagnosis.id
                }

            response = client.post(
                reverse(
                    url,
                    kwargs=kwargs,
                ),
                headers={"Hx-Request": "true"},
            )

            assert (
                response.status_code == HTTPStatus.OK
            ), f"{test_user} from {test_user.organisation_employer} with perms {test_user.groups.all()} request.POSTed to {url} for Case from {TEST_USER_ORGANISATION}. Expected {HTTPStatus.OK}, received {response.status_code}"

            # Additional test for RCPCH_AUDIT_TEAM and CLINICAL_AUDIT_TEAM adding in different Trust
            if test_user.first_name in [
                test_user_rcpch_audit_team_data.role_str,
                test_user_clinicial_audit_team_data.role_str,
            ]:
                response = client.post(
                    reverse(
                        url,
                        kwargs=kwargs,
                    ),
                    headers={"Hx-Request": "true"},
                )

                assert (
                    response.status_code == HTTPStatus.OK
                ), f"{test_user} from {test_user.organisation_employer} with perms {test_user.groups.all()} request.POSTed to {url} for Case from {DIFF_TRUST_DIFF_ORGANISATION}. Expected {HTTPStatus.OK}, received {response.status_code}"


@pytest.mark.django_db
def test_add_episode_comorbidity_syndrome_aem_forbidden(client):
    """
    Simulating different unauthorized E12 Roles adding Episodes for Case in same / diff Trust.

    - `add_episode`
    - `add_comorbidity`
    - `add_syndrome`
    - `add_antiepilepsy_medicine`

    """
    # set up constants

    # GOSH
    TEST_USER_ORGANISATION = Organisation.objects.get(
        ods_code="RP401",
        trust__ods_code="RP4",
    )

    # ADDENBROOKE'S
    DIFF_TRUST_DIFF_ORGANISATION = Organisation.objects.get(
        ods_code="RGT01",
        trust__ods_code="RGT",
    )

    CASE_FROM_SAME_ORG = Case.objects.get(
        first_name=f"child_{TEST_USER_ORGANISATION.name}"
    )

    CASE_FROM_DIFF_ORG = Case.objects.get(
        first_name=f"child_{DIFF_TRUST_DIFF_ORGANISATION.name}"
    )

    selected_users = [
        test_user_audit_centre_administrator_data.role_str,
        test_user_audit_centre_clinician_data.role_str,
        test_user_audit_centre_lead_clinician_data.role_str,
    ]

    users = Epilepsy12User.objects.filter(first_name__in=selected_users)

    if len(users) != len(selected_users):
        assert (
            False
        ), f"Incorrect number of users selected. Requested {len(selected_users)} but queryset contains {len(users)}: {users}"

    for test_user in users:
        client.force_login(test_user)

        URLS = [
            "add_episode",
            "add_comorbidity",
            "add_syndrome",
            "add_antiepilepsy_medicine",
        ]

        for url in URLS:
            if (
                test_user.first_name
                == test_user_audit_centre_administrator_data.role_str
            ):
                CASE = CASE_FROM_SAME_ORG

            # Other users only forbidden from doing action in different Trust
            else:
                CASE = CASE_FROM_DIFF_ORG

            if url == "add_antiepilepsy_medicine":
                kwargs = {
                    "management_id": CASE.registration.management.id,
                    "is_rescue_medicine": "is_rescue_medicine",
                }
            else:
                kwargs = {
                    "multiaxial_diagnosis_id": CASE.registration.multiaxialdiagnosis.id
                }

            response = client.post(
                reverse(
                    url,
                    kwargs=kwargs,
                ),
                headers={"Hx-Request": "true"},
            )

            assert (
                response.status_code == HTTPStatus.FORBIDDEN
            ), f"{test_user} from {test_user.organisation_employer} with perms {test_user.groups.all()} request.POSTed to `{url}` for Case from {CASE.organisations.all()}. Expected {HTTPStatus.FORBIDDEN}, received {response.status_code}"
