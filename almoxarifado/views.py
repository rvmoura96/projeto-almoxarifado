from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Equipamento, Item, Fabricante, Tipo, TipoItens, Modelo
from .forms import EquipForm, FabricanteForm, ItemForm, TipoEquipForm, TipoItemForm, ModeloForm
from .filters import EquipFilter, ItemFilter, FabFilter

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

def equip_filter(request):
    equip = Equipamento.objects.all()
    equip_filter = EquipFilter(request.GET, queryset=equip)
    return render(request, 'almoxarifado/equip_search.html', {'filter': equip_filter})

def item_filter(request):
    item = Item.objects.all()
    item_filter = ItemFilter(request.GET, queryset=item)
    return render(request, 'almoxarifado/item_search.html', {'filter': item_filter})

def fab_filter(request):
    fabricante = Fabricante.objects.all()
    fab_filter = FabFilter(request.GET, queryset=fabricante)
    return render(request, 'almoxarifado/fab_search.html', {'filter': fab_filter})

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

def fab_list(request):
    fabs = Fabricante.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(fabs, 5)
    try:
        fabs = paginator.page(page)
    except PageNotAnInteger:
        fabs = paginator.page(1)
    except EmptyPage:
        fabs = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/fab_list.html', {'fabs': fabs})

def model_list(request):
    models = Modelo.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(models, 5)
    try:
        models = paginator.page(page)
    except PageNotAnInteger:
        models = paginator.page(1)
    except EmptyPage:
        models = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/model_list.html', {'models': models})

def tipo_item_list(request):
    tipo_itens = TipoItens.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(tipo_itens, 5)
    try:
        tipo_itens = paginator.page(page)
    except PageNotAnInteger:
        tipo_itens = paginator.page(1)
    except EmptyPage:
        tipo_itens = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/tipo_item_list.html', {'tipo_itens': tipo_itens})

def tipo_equip_list(request):
    tipo_equips = Tipo.objects.filter()
    page = request.GET.get('page', 1)
    paginator = Paginator(tipo_equips, 5)
    try:
        tipo_equips = paginator.page(page)
    except PageNotAnInteger:
        tipo_equips = paginator.page(1)
    except EmptyPage:
        tipo_equips = paginator.page(paginator.num_pages)
    return render(request, 'almoxarifado/tipo_equip_list.html', {'tipo_equips': tipo_equips})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'almoxarifado/item_detail.html', {'item':item})

def equip_detail(request, pk):
    equip = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'almoxarifado/equip_detail.html', {'equip': equip})

def fab_detail(request, pk):
    fabricante = get_object_or_404(Fabricante, pk=pk)
    return render(request, 'almoxarifado/fab_detail.html', {'fabricante': fabricante})

def model_detail(request, pk):
    modelo  = get_object_or_404(Modelo, pk=pk)
    return render(request, 'almoxarifado/model_detail.html', {'modelo': modelo})

def item_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'almoxarifado/item_edit.html', {'form': form})

def model_new(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('model_detail', pk=model.pk)
    else:
        form = ModeloForm()
    return render(request, 'almoxarifado/model_edit.html', {'form': form})

def equip_new(request):
    if request.method == 'POST':
        form = EquipForm(request.POST)
        if form.is_valid():
            equip = form.save(commit=False)
            equip.save()
            return redirect('equip_detail', pk=equip.pk)
    else:
        form = EquipForm()
    return render(request, 'almoxarifado/equip_edit.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'almoxarifado/item_edit.html', {'form': form})

def equip_edit(request, pk):
    equip = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipForm(request.POST, instance=equip)
        if form.is_valid():
            equip = form.save(commit=False)
            equip.save()
            return redirect('equip_detail', pk=equip.pk)
    else:
        form = EquipForm(instance=equip)
    return render(request, 'almoxarifado/equip_edit.html', {'form': form})

def model_edit(request, pk):
    model = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        form = ModeloForm(request.POST, instance=model)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('model_detail', pk=model.pk)
    else:
        form = ModeloForm(instance=model)
    return render(request, 'almoxarifado/model_edit.html', {'form': form})

def fab_new(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            fabricante = form.save(commit=False)
            fabricante.save()
            return redirect('fab_detail', pk=fabricante.pk)
    else:
        form = FabricanteForm()
    return render(request, 'almoxarifado/fab_edit.html', {'form': form})

def fab_edit(request, pk):
    fabricante = get_object_or_404(Fabricante, pk=pk)
    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            fabricante = form.save(commit=False)
            fabricante.save()
            return redirect('fab_detail', pk=fabricante.pk)
    else:
        form = FabricanteForm(instance=fabricante)
    return render(request, 'almoxarifado/fab_edit.html', {'form': form})

def tipo_equip_new(request):
    if request.method == 'POST':
        form = TipoEquipForm(request.POST)
        if form.is_valid():
            tipo_equip = form.save(commit=False)
            tipo_equip.save()
            return redirect('tipo_equip_detail', pk=tipo_equip.pk)
    else:
        form = TipoEquipForm()
    return render(request, 'almoxarifado/tipo_edit.html', {'form': form})

def tipo_equip_detail(request, pk):
    tipo_equip = get_object_or_404(Tipo, pk=pk)
    return render(request, 'almoxarifado/tipo_equip_detail.html', {'tipo_equip': tipo_equip})

def tipo_equip_edit(request, pk):
    tipo_equip = get_object_or_404(Tipo, pk=pk)
    if request.method == 'POST':
        form = TipoEquipForm(request.POST, instance=tipo_equip)
        if form.is_valid():
            tipo_equip = form.save(commit=False)
            tipo_equip.save()
            return redirect('tipo_equip_detail', pk=tipo_equip.pk)
    else:
        form = TipoEquipForm(instance=tipo_equip)
    return render(request, 'almoxarifado/tipo_edit.html', {'form': form})

def tipo_item_new(request):
    if request.method == 'POST':
        form = TipoItemForm(request.POST)
        if form.is_valid():
            tipo_item = form.save(commit=False)
            tipo_item.save()
            return redirect('tipo_item_detail', pk=tipo_item.pk)
    else:
        form = TipoEquipForm()
    return render(request, 'almoxarifado/tipo_item_edit.html', {'form': form})

def tipo_item_detail(request, pk):
    tipo_item = get_object_or_404(TipoItens, pk=pk)
    return render(request, 'almoxarifado/tipo_item_detail.html', {'tipo_item': tipo_item})

def tipo_item_edit(request, pk):   
    tipo_item = get_object_or_404(TipoItens, pk=pk)
    if request.method == 'POST':
        form = TipoItemForm(request.POST, instance=tipo_item)
        if form.is_valid():
            tipo_item = form.save(commit=False)
            tipo_item.save()
            return redirect('tipo_item_detail', pk=tipo_item.pk)
    else:
        form = TipoItemForm(instance=tipo_item)
    return render(request, 'almoxarifado/tipo_item_edit.html', {'form': form})