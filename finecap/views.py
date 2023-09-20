from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
        else:
            print(form.errors)
            form = ReservaForm(request.POST)
    else:
        form = ReservaForm()

    return render(request, 'reservas/criarreserva.html', {'form': form})

def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'reservas/editarreserva.html',{'form':form})

def reserva_listar(request):
    reservas = Reserva.objects.all()
    context ={
        'reservas':reservas
    }
    return render(request, 'reservas/listarreserva.html',context)

def reserva_detalhar(request,id):
    reserva = Reserva.objects.get(id=id)
    return render(request,'reservas/detalhe.html', {'reserva': reserva})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')

def index(request):
    return render(request, 'reservas/index.html')