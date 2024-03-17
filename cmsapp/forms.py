from django import forms
from .models import DeptModel 
from .models import StudentModel

class DeptForm(forms.ModelForm) :
	class Meta :
		model = DeptModel
		fields = "__all__"


class StudentForm(forms.ModelForm) :
	class Meta :
		model = StudentModel
		fields = "__all__"
	