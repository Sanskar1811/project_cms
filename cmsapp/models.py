from django.db import models

# Create your models here.
class DeptModel(models.Model) :
	Department_Id = models.IntegerField(primary_key = True)
	Department_Name = models.CharField(max_length = 40)

	def __str__(self) :
		return self.Department_Name
	

class StudentModel(models.Model) :
	Student_Id = models.IntegerField(primary_key = True)
	Student_Name = models.CharField(max_length = 40)
	Student_Department = models.ForeignKey(DeptModel , on_delete = models.CASCADE)

	def __str__(self) :
		return self.Student_Department
	

	

	