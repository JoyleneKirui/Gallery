from django.shortcuts import render
from mygallery.models import pics

def displayimage(request):
    resultsdisplay = pics.objects.all()
    return render(request, 'home.html',{'pics':resultsdisplay})