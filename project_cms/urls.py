from django.contrib import admin
from django.urls import path
from cmsapp.views import home , addept , addstudent , showdept , showstud , removedept , removestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , home , name = "home"),
    path("addept" , addept , name = "addept"),
    path("addstudent" , addstudent , name = "addstudent"),
    path("showdept" , showdept , name = "showdept"),
    path("showstud" , showstud , name = "showstud"),
    path("removedept/<int:id>" , removedept , name = "removedept"),
    path("removestudent/<int:id>" , removestudent , name = "removestudent"),
]
