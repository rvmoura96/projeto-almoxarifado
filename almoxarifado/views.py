from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Equipamento, Item
from .forms import EquipForm

# Create your views here.

def equip_list(request):
    equips = Equipamento.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(equips, 5)
    try:
        equips = paginator.page(page)
    except PageNotAnInteger:
        equips = paginator.page(1)
    except EmptyPage:
        equips = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/equip_list.html', {'equips': equips})

def item_list(request):
    itens = Item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(itens, 5)
    try:
        itens = paginator.page(page)
    except PageNotAnInteger:
        itens = paginator.page(1)
    except EmptyPage:
        itens = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/item_list.html', {'itens': itens})

def general_list(request):
    equips = Equipamento.objects.order_by('-cadastro')[:5]
    itens = Item.objects.order_by('-cadastro')[:5]

    return render(request, 'almoxarifado/general_list.html', {'equips': equips,'itens': itens})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'almoxarifado/item_detail.html', {'item':item})

def equip_detail(request, pk):
    equip = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'almoxarifado/equip_detail.html', {'equip': equip})

def item_new(request):
    if request.method == 'POST':
        form = EquipForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('equip_detail', pk=item.pk)
    else:
        form = EquipForm()
    return render(request, 'almoxarifado/equip_edit.html', {'form': form})

def item_edit(request, pk):
    equip = get_object_or_404(Equipamento, pk=pk)
    if request.method =='POST':
        form = EquipForm(request.POST, instance=equip)
        if form.is_valid():
            equip = form.save(commit=False)
            equip.save()
            return redirect('equip_detail', pk=equip.pk)
    else:
        form = EquipForm(instance=equip)
    return render(request, 'almoxarifado/equip_edit.html', {'form': form})
