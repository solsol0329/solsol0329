from django.shortcuts import render
from datetime import datetime
# Create your views here.
def menus(request):
    menus = ['차돌된장', '돼지갈비찜']
    users = []
    context = {
        'menus': menus,
        'users': users,
        'today': datetime.today,
    }
    return render(request, 'menus/menus.html', context)
