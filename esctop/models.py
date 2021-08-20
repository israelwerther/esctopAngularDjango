from banco.models import Banco
from core.models import Contato, DadosPessoais, Endereco, Referencia, DadosDaEmpresa, DadosBancarios
from django.db import models


class Representante(models.Model):
    dados_pessoais = models.ManyToManyField(DadosPessoais, verbose_name=("Representante"))
    endereco = models.ManyToManyField(Endereco, verbose_name=("Endereço"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))

    class Meta:
        verbose_name = 'Representante'        

    def __str__(self):
        return self.dados_pessoais.nome

class ClienteEsctop(models.Model):
    dados_da_empresa = models.ForeignKey(DadosDaEmpresa, verbose_name=("Dados da empresa"), on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    banco = models.ForeignKey(Banco, verbose_name=("Banco"), on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(DadosBancarios, verbose_name=("Dados Bancários"), on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    representante = models.ManyToManyField(Representante, verbose_name=("Representante"))

    class Meta:
        verbose_name = 'Cliente Esctop'
        verbose_name_plural = 'Clientes Esctop'

    def __str__(self):
        return self.dados_da_empresa.razao_social