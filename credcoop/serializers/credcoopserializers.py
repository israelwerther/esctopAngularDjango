from banco.models import Banco
from core.models import Contato, DadosPessoais, Endereco, Referencia
from rest_framework import serializers
from credcoop.models import ClienteCredcoop


class DadosPessoaisSerializer(serializers.ModelSerializer):
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


class ReferenciaSerializer(serializers.ModelSerializer):
    # contatos = ContatoSerializer(many=True)
    # enderecos = EnderecoSerializer(many=True)
    class Meta:
        model = Referencia
        fields = '__all__'


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'


class ClienteCredcoopSerializer(serializers.ModelSerializer):

    dados_pessoais = DadosPessoaisSerializer()
    # contatos = ContatoSerializer(many=True)
    # enderecos = EnderecoSerializer(many=True)
    referencia = ReferenciaSerializer()
    banco = BancoSerializer()

    class Meta:
        model = ClienteCredcoop
        fields = ['id', 'dados_pessoais', 'contatos', 'enderecos', 'referencia', 'banco']