from django.shortcuts import render, redirect
from django.utils import timezone


from .models import *
from .forms import *

# Create your views here.

def agenda(request):
    homeworks = Homework.objects.all()
    form = HomeworkForm()
    date = timezone.datetime.now()


    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        'homeworks' : homeworks,
        'form' : form,
        'date' : date,
    }
    
    return render(request, 'agenda/agenda.html', context)



def edit_homework(request, primary_key):
    homework = Homework.objects.get(id=primary_key)

    form = HomeworkForm(instance=homework)

    # if request.method == 'POST':
    #     form = HomeworkForm(request.POST, instance=homework)
        
    #     if form.is_valid:
    #         form.save()
    #     return redirect('/')

    if request.method == 'POST':
        if 'editBtn' in request.POST:
            form = HomeworkForm(request.POST, instance=homework)
            if form.is_valid:
                form.save()
                return redirect('/')
        elif 'deleteBtn' in request.POST:
            homework.delete()
            return redirect('/')
    

    context = {
        'homework' : homework,
        'form' : form,
    }

    return render(request, 'agenda/edit_homework.html', context)

def create_subject(request):
    subjects = Subject.objects.all()
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        'subjects' : subjects,
        'form' : form
    }
    
    return render(request, 'agenda/create_subject.html', context)

