from core.models import Contato, DadosPessoais, Endereco, Referencia, DadosDaEmpresa
from django.db import models


class Empresa(models.Model):
    dados_da_empresa = models.ForeignKey(DadosDaEmpresa, verbose_name=("Dados da empresa"), on_delete=models.CASCADE)


class Representante(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, verbose_name=("Representante"), on_delete=models.CASCADE)    


class ClienteEsctop(models.Model):
    dados_da_empresa = models.ForeignKey(DadosDaEmpresa, verbose_name=("Dados da empresa"), on_delete=models.CASCADE)
    representante = models.ForeignKey(DadosPessoais, verbose_name=("Representante"), on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente Esctop'
        verbose_name_plural = 'Clientes Esctop'

    def __str__(self):
        return self.dados_da_empresa.razao_social