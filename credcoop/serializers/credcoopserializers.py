from banco.models import Banco
from emprestimo.models import Emprestimo
from core.models import Contato, DadosBancarios, DadosPessoais, Endereco, Referencia
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
    
    contatos = ContatoSerializer(many=True)
    class Meta:
        model = Referencia
        fields = '__all__'


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'
        
class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'  


class ClienteCredcoopSerializer(serializers.ModelSerializer):
    dados_pessoais = DadosPessoaisSerializer()
    contatos = ContatoSerializer(many=True)
    enderecos = EnderecoSerializer(many=True)
    referencias = ReferenciaSerializer(many=True)
    banco = BancoSerializer()
    dados_bancarios = DadosBancariosSerializer(many=True)
    emprestimos = EmprestimoSerializer(many=True)

    class Meta:
        model = ClienteCredcoop
        fields = ['id', 'dados_pessoais', 'contatos', 'enderecos', 'referencias', 'banco', 'dados_bancarios', 'emprestimos']