# # Estrutura de controle - Condicionais
# # Input - Entrada de dados; Int - Transforma o valor digitado em inteiro.
# idade = int(input("Digite sua idade: "))

# # Se satisfaz a condição, faça:
# if idade >= 18:
#     print ("No Brasil, você é maior de idade!")
# else:
#     print ("No Brasil, você não é maior de idade!")

# # IF - ELIF 
# nota = 75
# if nota >= 90:
#     print ("A")
# elif nota >= 80:
#     print ("B")
# elif nota >= 70:
#     print ("C")
# elif nota <=20:
#     print ("Reprovado")
# else:
#     print ("Nota abaixo de C")

# # #Loops - Laços de Repetição
# frutas = ['Uva', 'Tomate', 'Banana', 'Laranja']

# for fruta in frutas:
#     if fruta == 'Tomate':
#         break
#     print (fruta)

# for indice, fruta in enumerate(frutas):
#     #print("Indice: ", indice,", Fruta: ",fruta)
#     print(f"Indice:  {indice}, Fruta: {fruta}")
# for fruta in frutas:
#     print (fruta)

# for i in frutas:
#     print(i)

# for i in range(5):
#     print(i)

# # Looping Aninhado - Arrays bidimensionais
# for i in range(5):
#     for j in range (3):
#         print(f"i: {i}, j: {j}")

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for linha in matriz:
#     for elemento in linha:
#         print (elemento)

# # WHILE
# contador = 0
# while contador < 10:
#     print(contador)
#     contador += 1


# # FUNÇÕES
# # Função sem return, procedimento. Com parametro.
# def boasVindas(nome):
#     print(f"{nome}, seja bem vinda!!")
# #Invocando a função
# boasVindas('Bianca')

# # Função com return
# def boasVindas2(nome):
#     return (f"{nome}, seja bem vinda!!")


# aluna = input("Digite o seu nome: ")
# # Variável para receber o retorno da função. Invocando a função
# mensagem = boasVindas2(aluna)
# print(mensagem)

# Função sem parâmetros
def boasVindas3():
    print("Seja bem vinda!!")

boasVindas3()

def quadradoDeUmNumero(n):
    return (n*n)

print(quadradoDeUmNumero(3))