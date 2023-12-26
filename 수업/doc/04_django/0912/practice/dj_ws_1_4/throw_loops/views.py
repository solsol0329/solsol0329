from django.shortcuts import render

# Create your views here.
def first(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request,'first.html',context)     

def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request,'second.html',context)    

def third(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    context = {
        'message' : [message1,message2]
    }
    return render(request,'third.html',context)