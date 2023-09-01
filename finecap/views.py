from django.shortcuts import render, get_object_or_404,redirect
from .models import Reserva
from .forms import ReservaForm
# Create your views here.
def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES,instance=Reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas_listar')
    else:
        form = ReservaForm(instance=Reserva)

    return render(request,'reservas/editarreserva.html',{'form':form})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reservas/index.html') 

def reserva_detalhar(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    context ={
        'reserva':reserva
    }
    return render(request, "reservas/detalhe.html",context)

def criar_reserva(request):

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()
    
    return render(request,"reservas/criarreserva.html", {'form':form})

def index(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, "reservas/index.html",context)