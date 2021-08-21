from banco.models import Banco
from core.models import Contato, DadosBancarios, DadosDaEmpresa, Endereco, Referencia, DadosPessoais
from rest_framework import serializers
from esctop.models import ClienteEsctop, Representante


class DadosPessoaisSerializer(serializers.ModelSerializer):    
    class Meta:
        model = DadosPessoais
        fields = '__all__'


class DadosDaEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosDaEmpresa
        fields = '__all__'


class FiadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = '__all__'


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'        


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'

        
class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'       


class ReferenciaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Referencia
        fields = '__all__'


class RepresentanteSerializer(serializers.ModelSerializer):
    dados_pessoais = DadosPessoaisSerializer()
    endereco = EnderecoSerializer(many=True)
    contatos = ContatoSerializer(many=True)
    class Meta:
        model = Representante
        fields = '__all__'


class ClienteEsctopSerializer(serializers.ModelSerializer):   
    dados_da_empresa = DadosDaEmpresaSerializer()
    fiador = FiadorSerializer()
    contatos = ContatoSerializer(many=True)
    enderecos = EnderecoSerializer(many=True)
    banco = BancoSerializer()
    dados_bancarios = DadosBancariosSerializer()
    referencia = ReferenciaSerializer()
    representante = RepresentanteSerializer(many=True)

    class Meta:
        model = ClienteEsctop
        fields = [
            'id', 
            'dados_da_empresa', 
            'fiador', 
            'enderecos', 
            'contatos', 
            'banco', 
            'dados_bancarios', 
            'referencia', 
            'representante'
        ]