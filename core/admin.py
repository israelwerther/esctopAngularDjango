from core.models import Contato, DadosBancarios, DadosPessoais, Endereco, Referencia
from django.contrib import admin

admin.site.register(DadosPessoais)
admin.site.register(Contato)
admin.site.register(Endereco)
admin.site.register(Referencia)
admin.site.register(DadosBancarios)
