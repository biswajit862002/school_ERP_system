from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        # Validate that the email is unique.
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    


# ----------------------------------------------------------------------------------------------


# Student Management
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

# StudentRecord model
class StudentRecord(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='record')
    address = models.TextField()
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    additional_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Record of {self.student.name}"


class ICard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def __str__(self):
        return f"I-Card of {self.student.name}"


# Attendance Management
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"Attendance for {self.student.name} on {self.date}"


# Notification model
class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notifications')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.student.name} on {self.sent_at}"


# Financial Management
class FeeRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_mode = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Online', 'Online'), ('Cheque', 'Cheque')])

    def __str__(self):
        return f"Fee record for {self.student.name}"


class ESSLoan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approval_date = models.DateField()
    repayment_date = models.DateField()

    def __str__(self):
        return f"Loan for {self.student.name}"


# Inventory Management
class InventoryItem(models.Model):
    ITEM_CHOICES = [
        ('Dress', 'Dress'),
        ('Book', 'Book'),
        ('Shoes', 'Shoes'),
    ]
    name = models.CharField(max_length=50, choices=ITEM_CHOICES)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"


# Exam Management
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


class AdmitCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    issue_date = models.DateField()

    def __str__(self):
        return f"Admit Card for {self.student.name} - {self.exam.name}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"Result for {self.student.name} - {self.exam.name}"


# Activity Schedule
class Schedule(models.Model):
    ACTIVITY_CHOICES = [
        ('Class', 'Class'),
        ('Exam', 'Exam'),
        ('Sports', 'Sports'),
    ]
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} on {self.date}"

        
