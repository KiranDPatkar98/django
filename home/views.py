from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    people = [
        {"name": 'kdp', "age": 25},
        {"name": 'putta', "age": 27},
        {"name": 'pooja', "age": 13},
        {"name": 'jaggesh', "age": 40},
        {"name": 'sudeep', "age": 17},
        {"name": 'kohli', "age": 18},
    ]
    desc = ''' 
 Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque beatae nisi fuga esse?
   Ea temporibus rerum dicta dolor architecto dolorum suscipit aliquid, 
 explicabo facere? Veritatis fugiat enim minima voluptatibus voluptatum.
'''
    return render(request, 'home/index.html', context={'people': people, "text": desc})


def success_page(request):
    return HttpResponse('<h1>Iam success page</h1>')


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")
