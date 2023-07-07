# django
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.db.models.functions import Lower
from django.contrib.gis.db.models import UniqueConstraint

# 3rd party
from simple_history.models import HistoricalRecords

# rcpch
from epilepsy12.constants.user_types import (
    ROLES,
    TITLES,
    AUDIT_CENTRE_LEAD_CLINICIAN,
    TRUST_AUDIT_TEAM_FULL_ACCESS,
    AUDIT_CENTRE_CLINICIAN,
    TRUST_AUDIT_TEAM_EDIT_ACCESS,
    AUDIT_CENTRE_ADMINISTRATOR,
    TRUST_AUDIT_TEAM_EDIT_ACCESS,
    RCPCH_AUDIT_LEAD,
    EPILEPSY12_AUDIT_TEAM_FULL_ACCESS,
    RCPCH_AUDIT_ANALYST,
    EPILEPSY12_AUDIT_TEAM_EDIT_ACCESS,
    RCPCH_AUDIT_ADMINISTRATOR,
    EPILEPSY12_AUDIT_TEAM_VIEW_ONLY,
    RCPCH_AUDIT_PATIENT_FAMILY,
    PATIENT_ACCESS,
    TRUST_AUDIT_TEAM_VIEW_ONLY,
    AUDIT_CENTRE_MANAGER,
    VIEW_PREFERENCES,
)


class Epilepsy12UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.

    RCPCH Audit team members can be clinicians or RCPCH staff
    RCPCH staff cannot be associated with a organisation trust
    All clinicians must be associated with a organisation trust
    """

    def create_user(self, email, password, first_name, role, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        if not email:
            raise ValueError(_("You must provide an email address"))

        if not extra_fields.get("organisation_employer") and not extra_fields.get(
            "is_staff"
        ):
            # Non-RCPCH staff (is_staff) are not affiliated with a organisation
            raise ValueError(
                _("You must provide the name of your main organisation trust.")
            )

        if not role:
            raise ValueError(_("You must provide your role in the Epilepsy12 audit."))

        email = self.normalize_email(str(email))
        user = self.model(
            email=email,
            first_name=first_name,
            password=password,
            role=role,
            **extra_fields,
        )

        user.set_password(password)
        user.view_preference = 0  # organisation level view preference
        if not extra_fields.get("is_superuser"):
            user.is_superuser = False
        if not extra_fields.get("is_active"):
            user.is_active = False
        user.email_confirmed = False
        # user not active until has confirmed by email
        user.save()

        """
        Allocate Groups - the groups already have permissions allocated
        """
        if user.role == AUDIT_CENTRE_LEAD_CLINICIAN:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_FULL_ACCESS)
        elif user.role == AUDIT_CENTRE_CLINICIAN:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_EDIT_ACCESS)
        elif user.role == AUDIT_CENTRE_ADMINISTRATOR:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_VIEW_ONLY)
        elif user.role == AUDIT_CENTRE_MANAGER:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_VIEW_ONLY)
        elif user.role == RCPCH_AUDIT_LEAD:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_FULL_ACCESS)
        elif user.role == RCPCH_AUDIT_ANALYST:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_EDIT_ACCESS)
        elif user.role == RCPCH_AUDIT_ADMINISTRATOR:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_VIEW_ONLY)
        elif user.role == RCPCH_AUDIT_PATIENT_FAMILY:
            group = Group.objects.get(name=PATIENT_ACCESS)
        else:
            # no group
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_VIEW_ONLY)
        user.save()
        user.groups.add(group)

        print(f"creating {user} in {user.groups }")

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_rcpch_audit_team_member", True)
        extra_fields.setdefault("email_confirmed", True)
        # National level preference
        extra_fields.setdefault("view_preference", 2)

        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        logged_in_user = self.create_user(email, password, **extra_fields)

        """
        Allocate Roles
        """

        self.allocate_group_based_on_role(logged_in_user)

    def allocate_group_based_on_role(self, user):
        if user.role == AUDIT_CENTRE_LEAD_CLINICIAN:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_FULL_ACCESS)
            user.is_staff = True
        elif user.role == AUDIT_CENTRE_CLINICIAN:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_EDIT_ACCESS)
            user.is_staff = True
        elif user.role == AUDIT_CENTRE_ADMINISTRATOR:
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_EDIT_ACCESS)
            user.is_staff = True
        elif user.role == RCPCH_AUDIT_LEAD:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_FULL_ACCESS)
            user.is_staff = True
        elif user.role == RCPCH_AUDIT_ANALYST:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_EDIT_ACCESS)
            user.is_staff = True
        elif user.role == RCPCH_AUDIT_ADMINISTRATOR:
            group = Group.objects.get(name=EPILEPSY12_AUDIT_TEAM_VIEW_ONLY)
        elif user.role == RCPCH_AUDIT_PATIENT_FAMILY:
            group = Group.objects.get(name=PATIENT_ACCESS)
        else:
            # no group
            group = Group.objects.get(name=TRUST_AUDIT_TEAM_VIEW_ONLY)
        user.groups.add(group)


class Epilepsy12User(AbstractUser, PermissionsMixin):
    username = None
    first_name = models.CharField(
        _("First name"),
        help_text=_("Enter your first name"),
        max_length=150,
        null=True,
        blank=True,
    )
    surname = models.CharField(
        _("Surname"),
        help_text=_("Enter your surname"),
        max_length=150,
        null=True,
        blank=True,
    )
    title = models.PositiveSmallIntegerField(choices=TITLES, blank=True, null=True)
    email = models.EmailField(
        _("Email address"),
        help_text=_("Enter your email address."),
        unique=True,
        error_messages={"unique": _("This email address is already in use.")},
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        # reflects if user has access to admin
        default=False
    )
    is_superuser = models.BooleanField(default=False)
    is_rcpch_audit_team_member = models.BooleanField(
        # reflects is a member of the RCPCH audit team. If is_clinician is true, user is also a clinician and therefore must
        # may be affiliated with a organisation trust
        default=False
    )
    is_clinician = models.BooleanField(
        # reflects is a clinician
        # must be affiliated with an organisation
        default=False
    )
    is_patient_or_carer = models.BooleanField(
        # reflects is a patient or carer
        # must be affiliated with an organisation
        default=False
    )
    view_preference = models.SmallIntegerField(
        choices=VIEW_PREFERENCES,
        default=0,  # Organisation level is default
        blank=False,
        null=False,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)

    history = HistoricalRecords()

    REQUIRED_FIELDS = ["role", "first_name", "surname", "is_rcpch_audit_team_member"]
    USERNAME_FIELD = "email"

    objects = Epilepsy12UserManager()

    organisation_employer = models.ForeignKey(
        "epilepsy12.Organisation", on_delete=models.CASCADE, blank=True, null=True
    )

    def get_full_name(self):
        title = self.get_title_display()
        concatenated_name = ""
        if title:
            concatenated_name += f"{title} "
        if self.first_name:
            concatenated_name += f"{self.first_name} "
        if self.surname:
            concatenated_name += f"{self.surname}"
        return concatenated_name

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Epilepsy12 User"
        verbose_name_plural = "Epilepsy12 Users"
        constraints = [
            UniqueConstraint(
                Lower("email"),
                name="user_email_ci_uniqueness",
            ),
        ]

    def __str__(self) -> str:
        return self.get_full_name()
