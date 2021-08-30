from django.contrib.auth.models import User
from django.db import models


class Emprestimo(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    valor_do_emprestimo = models.CharField("Valor do Empréstimo", max_length=50)
    parcelas = models.CharField("Parcelas", max_length=50)
    contrato = models.CharField("Contrato", max_length=50, null=True, unique=True)
    
    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return self.valor_do_emprestimo
