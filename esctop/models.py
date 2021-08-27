from banco.models import Banco
from core.models import Contato, DadosPessoais, Endereco, Referencia, DadosDaEmpresa, DadosBancarios
from django.db import models
from emprestimo.models import Emprestimo


class RepresentanteEsctop(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    endereco = models.ManyToManyField(Endereco, verbose_name=("Endereço"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))

    class Meta:
        verbose_name = 'Representante Esctop'
        verbose_name_plural = 'Representantes Esctop'
    
    def __str__(self):
        return self.dados_pessoais.nome


class FiadorEsctop(models.Model):
    dados_pessoais = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereço"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    banco = models.ForeignKey(Banco, verbose_name=("Banco"), on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(DadosBancarios, verbose_name=("Dados Bancários"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Fiador Esctop'
        verbose_name_plural = 'Fiadores Esctop'
    
    def __str__(self):
        return self.dados_pessoais.nome


class ClienteEsctop(models.Model):
    dados_da_empresa = models.ForeignKey(DadosDaEmpresa, verbose_name=("Dados da empresa"), on_delete=models.CASCADE)
    fiador_esctop = models.ManyToManyField(FiadorEsctop, verbose_name=("Fiador Esctop"))
    enderecos = models.ManyToManyField(Endereco, verbose_name=("Endereços"))
    contatos = models.ManyToManyField(Contato, verbose_name=("Contatos"))
    banco = models.ForeignKey(Banco, verbose_name=("Banco"), on_delete=models.CASCADE)
    dados_bancarios = models.ForeignKey(DadosBancarios, verbose_name=("Dados Bancários"), on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    representante_esctop = models.ManyToManyField(RepresentanteEsctop, verbose_name=("Representante Esctop"))
    emprestimo = models.ForeignKey(Emprestimo, verbose_name=("Emprestimos"), on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente Esctop'
        verbose_name_plural = 'Clientes Esctop'

    def __str__(self):
        return self.dados_da_empresa.razao_social