from django.shortcuts import render, redirect
from .models import Reciepe

# Create your views here.


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
