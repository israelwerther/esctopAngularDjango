from django.contrib import admin
from emprestimo.models import Emprestimo

# admin.site.register(Emprestimo)
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(       
        'id', 
        'contrato',
        'valor_do_emprestimo',
        'parcelas',
        'funcionario',
    )
    search_fields=('id', 'contrato', 'valor_do_emprestimo', 'parcelas',)
    list_filter=('funcionario', 'valor_do_emprestimo', 'parcelas', 'contrato',)