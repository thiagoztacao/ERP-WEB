"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import XMLFile, Cliente, Produto, Pedido


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class XMLFileForm(forms.ModelForm):
    class Meta:
        model = XMLFile
        fields = ['xml_file']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'telefone', 'endereco')

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('sku', 'descricao', 'valor')

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'data_pedido', 'valor_total')