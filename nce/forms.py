from .models import Feedback
from django import forms



class ContactForm(forms.ModelForm):


	class Meta:
		model = Feedback
		fields = '__all__'