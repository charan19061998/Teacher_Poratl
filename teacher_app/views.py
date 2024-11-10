from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import *
from .models import Student
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def Signup(request):
    if request.method == 'POST':
        fm=Signup_Form(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
    else:
        fm=Signup_Form()
    return render(request,'signup.html',{'form':fm})


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/home')  # Redirect after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please enter valid login details.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def home_view(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

@login_required
def add_student(request):
    """Add a new student record or show error if record already exists."""
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            sub = fm.cleaned_data['subject']
            marks = fm.cleaned_data['marks']

            # Check if a student with the same name and subject already exists
            existing_student = Student.objects.filter(name=nm, subject=sub).exists()

            if existing_student:
                # If a student with the same name and subject exists, show an error message
                messages.error(request, "Student record already exists!")
                return render(request, 'add_student.html', {'form': fm})  # Stay on the same page
            else:
                # If no matching student is found, create a new student record
                student = Student(name=nm, subject=sub, marks=marks)
                student.save()
                return redirect('/home')  # Redirect to home after the operation
    else:
        fm = StudentForm()

    # Get all students to display in the template
    student = Student.objects.all()
    return render(request, 'add_student.html', {'form': fm, 'student': student})

@login_required
def update_student(request,id):
    pi=Student.objects.get(pk=id)
    if request.method=="POST":
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm=StudentForm(instance=pi)
    return render(request,'update_student.html',{'form':fm})

@login_required
def delete_student(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home')


