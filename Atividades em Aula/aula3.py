# DICIONÁRIO E OBJETO
 # DICIONÁRIO
 # Estrutura de chave-valor
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
pessoa = {
    'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'
    }
print(pessoa['nome'])
 
# OBJETO
# Sempre letra maiúscula no início de uma classe
 
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        
pessoa = Pessoa(nome='João', idade=25, cidade='São Paulo')
print(pessoa.nome)