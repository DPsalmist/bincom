from django import forms
from django.forms import ModelForm

from .models import POLLING_UNIT

class PollForm(forms.ModelForm):
	class Meta:
		model = POLLING_UNIT
		fields = '__all__'

