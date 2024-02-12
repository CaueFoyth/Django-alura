from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

# Serializer serve para filtrar os dados da API, se quiser todos os dados basta colocar '__all__', ou selecionar um a um com uma lista como ['id', 'nome']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #Usado para excluir um campo exemplo 'id', como está vazio irá puxar todos