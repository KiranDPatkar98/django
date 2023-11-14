from django.shortcuts import render, redirect
from .models import Reciepe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as session, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def reciepes(request):
    # To fetch the information from the post
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        reciepe = Reciepe(name=name, description=description, image=image)
        reciepe.save()
        # Reciepe.objects.create(
        #     name=name,
        #     description=description,
        #     image=description
        # )
        return redirect('/reciepes/')

    # To send the information to the page
    query_set = Reciepe.objects.all()

    # For searched values
    if request.GET.get('search'):
        query_set = query_set.filter(name__icontains=request.GET.get('search'))

    return render(request, 'reciepes.html', context={"reciepes": query_set})


def update_reciepe(request, id):
    query_set = Reciepe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        query_set.name = name
        query_set.description = description

        if image:
            query_set.image = image

        query_set.save()
        return redirect('/reciepes/')

    return render(request, 'update-reciepes.html', context={"reciepe": query_set})


def delete_reciepe(request, id):
    query_set = Reciepe.objects.get(id=id)
    query_set.delete()

    return redirect('/reciepes/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Invalid credentials")
            else:
                session(request, user)
                return redirect('/reciepes/')

        else:
            messages.error(request, "Username not found")
            return redirect('/login/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already exists.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created sucessfully")
        return redirect('/register/')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login')
