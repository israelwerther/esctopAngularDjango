from banco.models import Banco
from core.models import Contato, DadosBancarios, DadosPessoais, Endereco, Referencia
from django.db import models


class ClienteCredcoop(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, verbose_name=("Dados pessoais"), on_delete=models.CASCADE)
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, verbose_name=("Banco"), on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(DadosBancarios, verbose_name=("Dados Bancários"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente Credcoop'
        verbose_name_plural = 'Clientes Credcoop'

    def __str__(self):
        return self.dados_pessoais.nome
