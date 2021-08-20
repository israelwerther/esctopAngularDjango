from core.models import Contato, DadosBancarios, DadosDaEmpresa, DadosPessoais, Endereco, Referencia
from django.contrib import admin

admin.site.register(Contato)
admin.site.register(DadosPessoais)
admin.site.register(DadosDaEmpresa)
admin.site.register(Endereco)
admin.site.register(Referencia)
admin.site.register(DadosBancarios)
