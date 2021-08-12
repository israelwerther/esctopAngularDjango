from core.models import Contato, DadosPessoais, Endereco, Referencia
from django.db import models

class Representante(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, verbose_name=("Representante"), on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))

class Empresa(models.Model):
    razao_social = models.CharField("Razão Social", max_length=50)
    nome_fantasia = models.CharField("Nome Fantasia", max_length=50)
    cnpj = models.CharField("CNPJ", max_length=36, unique=True)
    fundacao = models.DateField("Fundação",max_length=8)
    inscricao_estadual = models.CharField("Inscrição Estadual", max_length=50)
    inscricao_municipal = models.CharField("Inscrição Municipal",max_length=50)

class ClienteEsctop(models.Model):
    representante = models.ForeignKey(DadosPessoais, verbose_name=("Representante"), on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente Esctop'
        verbose_name_plural = 'Clientes Esctop'

    def __str__(self):
        return self.dados_pessoais.nome