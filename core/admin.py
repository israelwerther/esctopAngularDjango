from core.models import Contato, DadosBancarios, DadosDaEmpresa, DadosPessoais, Endereco, LocalDeTrabalho, Referencia
from django.contrib import admin

admin.site.register(DadosPessoais)
admin.site.register(LocalDeTrabalho)
admin.site.register(DadosDaEmpresa)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(Referencia)
admin.site.register(DadosBancarios)
