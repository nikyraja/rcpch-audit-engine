from django_unicorn.components import UnicornView
from ..models import DESSCRIBE, Registration


class NonepilepticSeizureOnsetView(UnicornView):
    case_id = ""
    registration = Registration.objects.none()
    desscribe = DESSCRIBE.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        if (kwargs.get('registration')):
            self.registration = kwargs.get('registration')
            if DESSCRIBE.objects.filter(registration=self.registration).exists():
                self.desscribe = DESSCRIBE.objects.filter(
                    registration=self.registration).first()
