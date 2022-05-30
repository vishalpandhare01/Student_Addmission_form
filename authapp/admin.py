from django.contrib import admin
from .models import StudentReg,AddmisionForm


# Register your models here.
class DisplayAdmissionForm(admin.ModelAdmin):
    list_display=('photo','full_name','fathare_name','Phone_Number','adhar_number','Address','date','age','gender')


admin.site.register(StudentReg)
admin.site.register(AddmisionForm,DisplayAdmissionForm)