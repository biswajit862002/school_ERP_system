from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Student)
admin.site.register(Notification)



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_number', 'date_of_birth', 'address', 'email', 'phone_number', 'guardian_name', 'guardian_contact']


@admin.register(StudentRecord)
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ['id','student', 'address', 'guardian_name', 'guardian_contact', 'additional_notes']


@admin.register(ICard)
class ICardAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'issue_date', 'expiry_date']    


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'date', 'status'] 


@admin.register(FeeRecord)
class FeeRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'amount_paid', 'payment_date', 'payment_mode']


@admin.register(ESSLoan)
class ESSLoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'loan_amount', 'approval_date', 'repayment_date']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'ITEM_CHOICES', 'name', 'quantity', 'last_updated']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']


@admin.register(AdmitCard)
class AdmitCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'exam', 'issue_date']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'exam', 'marks_obtained', 'grade']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'ACTIVITY_CHOICES', 'activity_type', 'description', 'date']