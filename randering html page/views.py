from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("This is About Us")
def contactUs(request):
    return HttpResponse("This is Contact")

# dynamic urls
def course(request):
    return HttpResponse("Course Main Page")


def courseDetail(request,courseID):
    return HttpResponse(courseID)

# redering html page
def homePage(request):
    return render(request,"index.html")
