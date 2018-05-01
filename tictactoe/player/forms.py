from django.forms import ModelForm
from .models import Welcome


class NameForm(ModelForm):
    class Meta:
        model = Welcome
        exclude = ()

