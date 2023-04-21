"""
Definition of models.
"""

from django.db import models

class XMLFile(models.Model):
    xml_file = models.FileField(upload_to='xml_files/')

    def __str__(self):
        return self.xml_file.name

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    class Meta:
        app_label = 'app'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        app_label = 'app'

class Produto(models.Model):
    sku = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField(max_length=10)
    class Meta:
        app_label = 'app'

