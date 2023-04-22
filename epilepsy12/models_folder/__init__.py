
# These models represent the individual fields that clinicians must score
# and drive the forms and templates in the audit.
# Their division into discrete files is purely for semantic reasons as
# they are all linked in a one to one relationship with Registration,
# which in turn has a one to one relationship with Case
# The exceptions to this are:
# - AntiEpilepsyMedicine: this has a many to one relationship with Management,
#   and a one to many relationship with MedicineEntity
# - Comorbidity: this has a many to one relationship with Management,
#   and a one to many relationship with ComorbidityEntity
# - Episode: this has a many to one relationship with MultiaxialDiagnosis,
# - Site: this has a many to one relationship with Case,
#   and a one to many relationship with Organisation
# - Syndrome: this has a many to one relationship with MultiaxialDiagnosis,
#   and a many to one relationship with SyndromeEntity

from .antiepilepsy_medicine import AntiEpilepsyMedicine
from .assessment import Assessment
from .case import Case
from .comorbidity import Comorbidity
from .epilepsy_context import EpilepsyContext
from .first_paediatric_assessment import FirstPaediatricAssessment
from .investigations import Investigations
from .management import Management
from .registration import Registration
from .epilepsy12_site import Site
from .epilepsy12user import Epilepsy12User
from .episode import Episode
from .syndrome import Syndrome
from .multiaxial_diagnosis import MultiaxialDiagnosis

# These are models which store progress, either of each child in the audit,
# or each child's performance indicator score
# or every E12 user's activity
from .audit_progress import AuditProgress
from .kpi import KPI
from .visitactivity import VisitActivity

# These are helper classes to support the functioning of each model. Do not need to be globally available
from .time_and_user_abstract_base_classes import TimeStampAbstractBaseClass, UserStampAbstractBaseClass
from .help_text_mixin import HelpTextMixin

# clinical entities seeded from clinical APIs (eg SNOMED CT)
# These tables provide look ups to Epilepsy12 selects
from .entities.syndrome_entity import SyndromeEntity
from .entities.epilepsy_cause_entity import EpilepsyCauseEntity
from .entities.comorbidy_entity import ComorbidityEntity
from .entities.medicine_entity import MedicineEntity
from .semiology_keyword import Keyword

# regional entities seeded from NHS / ONS APIs
# These tables provide levels of abstraction
# when calculating KPIs. NHS Structure is often subject to change, so having their
# own model(s) abstracts away any changes that may need to be made in future.
# Organisation has many to one relationship with OPENUKNetworkEntity, IntegratedCareBoardEntity,
# CountryONSRegionEntity and NHSRegionEntity
# IntegratedCareBoardEntity has a one to many relationship with NHSRegionEntity
from .entities.open_uk_network_entity import OPENUKNetworkEntity
from .entities.integrated_care_board_entity import IntegratedCareBoardEntity
from .entities.country_ons_region_entity import CountryONSRegionEntity
from .entities.nhs_region_entity import NHSRegionEntity
from .entities.organisation import Organisation
