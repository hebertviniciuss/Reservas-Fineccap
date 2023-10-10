from django.shortcuts import render,get_object_or_404,redirect
from .models import Reserva
from django.db.models.query import QuerySet
from .forms import ReservaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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
    if(request.GET.get('search-name')):
        reservas = reservas.filter(nome_empresa__icontains=request.GET.get('search-name'))
    if(request.GET.get('search-payed-true')):
        reservas = reservas.filter(quitado=True)
    if(request.GET.get('search-payed-false')):
        reservas = reservas.filter(quitado=False)
    if(request.GET.get('search-value')):
        reservas = reservas.filter(stand__valor=request.GET.get('search-value'))
    if(request.GET.get('search-date')):
        reservas = reservas.filter(data_reserva__date=request.GET.get('search-date'))    
       
    paginator = Paginator(reservas, 5)
    page = request.GET.get('page')
    try:
        reservas = paginator.page(page)
    except PageNotAnInteger:
        reservas = paginator.page(1)
    except EmptyPage:
        reservas = paginator.page(paginator.num_pages)
        
    context ={
        'reservas':reservas
    }
    return render(request, 'reservas/listarreserva.html',context)

def reserva_detalhar(request,id):
    reserva = Reserva.objects.get(id=id)
    return render(request,'reservas/detalhe.html', {'reserva': reserva})

@login_required(login_url='/login/')
def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')

def index(request):
    return render(request, 'reservas/index.html')