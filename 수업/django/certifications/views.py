from django.shortcuts import render
import random
# Create your views here.

age = range(25,31)
grade = ['a','b','c','s']


def certification1(request):
    context={
        'age':random.choice(age),
        'grade':random.choice(grade),
        'names':"김남길",
    }
    return render(request, 'certifications/certification1.html',context)

def certification2(request):
    context={
    'age':random.choice(age),
    'grade':random.choice(grade),
    'names':"한소희",
}
    return render(request, 'certifications/certification2.html',context)

def certification3(request):
    context={
    'age':random.choice(age),
    'grade':random.choice(grade),
    'names':"남궁민",
}
    return render(request, 'certifications/certification3.html',context)
