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

    return render(request, 'reciepes.html', context={"reciepes": query_set})


def delete_reciepe(request, id):
    query_set = Reciepe.objects.get(id=id)
    print(query_set)
    query_set.delete()

    return redirect('/reciepes/')
