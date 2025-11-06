from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse

from .models import Cultivo
from .forms import CultivoForm


def my_cultivos(request):
    myCultivos = get_list_or_404(Cultivo, farmer=request.user)
    context = {'myCultivos': myCultivos}

    return render (request, 'cultivos/Mis_Cultivos.html', context)

def details_cultivo(request, cultivo_id):
    cultivo = get_object_or_404(Cultivo, pk=cultivo_id)
    context = {'cultivo': cultivo}

    return render(request, 'cultivos/cultivo_details.html', context)

def create_cultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            cultivo = form.save(commit=False)
            cultivo.farmer = request.user
            cultivo = form.save()
            return redirect(reverse('cultivos:mis_cultivos'))
    else:
        form = CultivoForm()
    
    return render(request, 'cultivos/create_cultivo.html', {'form': form})

def edit_cultivo(request, pk):
    cultivoInstance = get_object_or_404(Cultivo, pk=pk)

    if request.method == 'POST':
        form = CultivoForm(request.POST, instance=cultivoInstance)
        if form.is_valid():
            cultivo = form.save(commit=False)
            cultivo.farmer = request.user
            cultivo = form.save()
            return redirect(reverse('cultivos:mis_cultivos'))
    else:
        form = CultivoForm(instance=cultivoInstance)
    return render(request, 'cultivos/edit_cultivo.html', {'form': form})
    
def delete_cultivo(request, pk):
    cultivoToDelete = get_object_or_404(Cultivo, pk=pk)

    if request.method =='POST':
        cultivoToDelete.delete()
        return redirect('cultivos:mis_cultivos')
    return render(request, 'cultivos/confirm_delete.html', {'cultivoToDelete': cultivoToDelete})