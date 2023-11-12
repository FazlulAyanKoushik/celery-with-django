from django.http import HttpResponse
from django.shortcuts import render

from project.celery import add
from .tasks import test_func


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")


def home(request):
    print("Home : ")
    result = add.delay(5, 9)
    print("result : ", result)
    return render(request, "my_app/home.html")


def about(request):
    print("about : ")
    return render(request, "my_app/about.html")


def contact(request):
    print("contact : ")
    return render(request, "my_app/contact.html")
