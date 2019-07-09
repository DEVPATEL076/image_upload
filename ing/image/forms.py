from django import forms
from .models import *

class img_stor(forms.ModelForm):

	class Meta():
		model=demo
		fields=['name','img']