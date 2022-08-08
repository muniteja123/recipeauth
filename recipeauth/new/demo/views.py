from django.shortcuts import render,get_object_or_404
from . models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def reg(request):
    if request.method == 'POST':
        MyUser.objects.create_user(
            email=request.POST["email"],
            password=request.POST["password"],
        )
        return HttpResponseRedirect("/demo/")
    return render(request, "demo/reg.html")


def login_info(request):
    return render(request, 'demo/login_info.html')


def validate(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/demo/home/')
    else:
        return HttpResponse("<h1>User is not registered<h1>")


def logout_info(request):
    logout(request)
    return HttpResponseRedirect("/demo/")

@login_required(login_url='menu/')
def home(request):
   # import pdb; pdb.set_trace()
    context = Menu.objects.all()
    return render(request, "demo/home.html", {"context": context})

@login_required
def process(request):
    if request.method == 'POST':
        Menu.objects.create(
            name=request.POST["name"],
            ingrediants=request.POST["ingrediants"],
            process=request.POST["process"],
        )
      #  return HttpResponseRedirect(reverse("menu:home"))
        return HttpResponseRedirect("/demo/home/")
    return render(request, "demo/process.html")

@login_required(login_url='demo/')
def details(request, recipe_id):
    con = get_object_or_404(Menu, pk=recipe_id)
    return render(request, "demo/details.html", {"con": con})

