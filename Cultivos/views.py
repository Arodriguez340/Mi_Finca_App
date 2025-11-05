from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Cultivo


def my_cultivos(request):
    myCultivos = get_list_or_404(Cultivo, farmer=request.user)
    context = {'myCultivos': myCultivos}

    return render (request, 'Cultivos/Mis_Cultivos.html', context)

def details_cultivo(request, cultivo_id):
    cultivo = get_object_or_404(Cultivo, pk=cultivo_id)
    context = {'cultivo': cultivo}

    return render(request, 'cultivos/cultivo_details.html', context)

