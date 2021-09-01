from emprestimo.models import Emprestimo
from banco.models import Banco
from core.models import Contato, DadosBancarios, DadosPessoais, Endereco, LocalDeTrabalho, Referencia
from django.db import models


class ClienteCredcoop(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, verbose_name=("Dados pessoais"), on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    localDeTrabalho = models.ManyToManyField(LocalDeTrabalho, verbose_name="Local de Trabalho")
    referencias = models.ManyToManyField(Referencia, verbose_name=("Referências"))
    banco = models.ForeignKey(Banco, verbose_name=("Banco"), on_delete=models.CASCADE)
    dados_bancarios = models.ManyToManyField(DadosBancarios, verbose_name=("Dados Bancários"))
    emprestimos = models.ManyToManyField(Emprestimo, verbose_name=("Emprestimos"))

    class Meta:
        verbose_name = 'Cliente Credcoop'
        verbose_name_plural = 'Clientes Credcoop'

    def __str__(self):
        return self.dados_pessoais.nome
