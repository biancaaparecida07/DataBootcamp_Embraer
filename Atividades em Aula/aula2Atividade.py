# Escreva um script que pergunte ao usuário a quantidade de quilometragem percorrido por um carro que ele alugou. 
km = int(input("Qual a quilometragem percorrida pelo carro que você alugou?"))
dias = int(input ("Quantos dias alugados?"))
# Calcule o preço a pagar, sendo que o valor da diária é de R$60 e o preço por quilômetro é de R$0,15.
precoKM = 0.15
precoDiaria = 60

valorPagar = (precoKM*km)+(precoDiaria*dias)
print(f"O valor a pagar é de R${valorPagar}")

#_______________________________________________________________________________
#Faça um script que exiba as tabuadas de 1 até 10 no formato 2 * 3 = 6
for i in range(1,11):
    for j in range (1,11):
        resultado = i*j
        print(f"{i} x {j} = {resultado}")

#_______________________________________________________________________________
#Faça um script que inicialize uma lista vazia, solicite ao usuário 10 numeros ímpares diferentes, um por vez. Caso o número digitado seja par, solicite novamente um número até que o valor seja um número ímpar. Depois disso, exiba os 10 números digitados. 
# #Loops - Laços de Repetição
impares = []
for i in range (1,11):
    numero = int(input ('Digite um número ímpar:'))
    while(numero%2==0):
        numero = int(input ('Digite um número ímpar:'))
    impares.append(numero)
print(impares)
