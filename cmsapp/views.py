from django.shortcuts import render , redirect
from .models import DeptModel , StudentModel
from .forms import DeptForm , StudentForm

# Create your views here.
def home(request) :
	return render(request , "home.html")


def addept(request) :
	if request.method == "POST" :
		data = DeptForm(request.POST)
		if data.is_valid() :
			data.save()	
			msg = "Records saved"
			fm = DeptForm()
			return render(request , "addept.html" , {"fm" : fm , "msg" : msg})
		else :
			msg = "Check errors"
			fm = DeptForm()
			return render(request , "addept.html" , {"fm" : data , "msg" : msg})
	else :
		fm = DeptForm()
		return render(request , "addept.html" , {"fm" : fm})

def addstudent(request) :
	if request.method=="POST" :
		data = StudentForm(request.POST)
		if data.is_valid() :
			data.save()
			fm = StudentForm()
			msg = "Records Saved"
			return render(request , "addstudent.html" , {"fm" : fm , "msg" : msg})
		else :
			fm = StudentForm()
			msg = "Check Errors"
			return render(request , "addstudent.html" , {"fm" : fm , "msg" : msg})
	else :
		fm = StudentForm()
		return render(request , "addstudent.html" , {"fm" : fm})

def showstud(request) :
	data = StudentModel.objects.all()
	return render(request , "showstud.html" , {"data" : data})

def showdept(request) :
	data = DeptModel.objects.all()
	return render(request , "showdept.html" , {"data" : data})


def removedept(request , id):
	dp = DeptModel.objects.get(Department_Id=id)
	dp.delete()
	return redirect("showdept")

def removestudent(request , id):
	dp = StudentModel.objects.get(Student_Id=id)
	dp.delete()
	return redirect("showstud")