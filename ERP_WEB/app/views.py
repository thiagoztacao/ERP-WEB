"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import XMLFileForm
from .models import Cliente, Produto, Pedido
from .forms import ClienteForm, ProdutoForm, PedidoForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def calculadora(request):
    if request.method == 'POST':
        form = XMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'calculadora.html', {'form': form, 'success': True})
    else:
        form = XMLFileForm()
    return render(request, 'calculadora.html', {'form': form})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecionar para a p�gina de sucesso
    else:
        form = ClienteForm()
    return render(request, 'criar_cliente.html', {'form': form})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecionar para a p�gina de sucesso
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecionar para a p�gina de sucesso
    else:
        form = PedidoForm()
    return render(request, 'criar_pedido.html', {'form': form})

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})

def pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido.html', {'pedidos': pedidos})

def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': produtos})