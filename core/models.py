from django.db import models

class DadosPessoais(models.Model):
    nome = models.CharField("Nome", max_length=50)
    rg = models.CharField("RG", max_length=50)
    cpf = models.CharField("CPF", max_length=50)

    class Meta:
        verbose_name_plural = 'Dados Pessoais'

    def __str__(self):
        return self.nome


class DadosDaEmpresa(models.Model):
    razao_social          = models.CharField("Razão ", max_length=50, blank=True, null=True)
    nome_fantasia         = models.CharField("Nome Fantasia", max_length=50, blank=True, null=True)
    cnpj                  = models.CharField("CNPJ", max_length=36, unique=True, blank=True, null=True)
    fundacao              = models.DateField("Fundação",max_length=8, blank=True, null=True)      
    inscricao_estadual    = models.CharField("Inscrição Estadual",blank=True, null=True, max_length=50)
    inscricao_municipal   = models.CharField("Inscrição Municipal", blank=True, null=True,max_length=50)

    class Meta:
        verbose_name_plural = 'Razão Social'

    def __str__(self):
        return self.razao_social


class Endereco(models.Model):
    cep = models.CharField("Cep", max_length=50)
    rua = models.CharField("Rua", max_length=50)
    numero = models.CharField("Número", max_length=50)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.cep

class Contato(models.Model):
    numero = models.CharField("Número", max_length=50)
    whatsapp = models.BooleanField("É whatsapp?", default=False)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.numero


class Referencia(models.Model):
    nome = models.CharField("Nome", max_length=50)
    endereco = models.CharField("Parentesco", max_length=50, blank=True)
    contatos = models.ManyToManyField(Contato)

    class Meta:
        verbose_name = 'Referência'
        verbose_name_plural = 'Referências'

    def __str__(self):
        return self.nome


class DadosBancarios(models.Model):     
    n_operacao            = models.CharField("Nº operação",max_length=15, blank=True)
    tipo_de_conta         = models.CharField('Tipo de conta', max_length=25, blank=True)  
    agencia               = models.CharField("Nº agência",max_length=15, blank=True)
    conta                 = models.CharField("Nº conta",max_length=15, blank=True)
    
    class Meta:
        verbose_name = 'Dado Bancário'
        verbose_name_plural = 'Dados Bancários'

    def __str__(self):
        return self.tipo_de_conta

    