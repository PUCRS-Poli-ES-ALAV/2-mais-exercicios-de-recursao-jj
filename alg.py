# Exercício 1
# Modele e implemente um método recursivo que calcule o fatorial de um número n passado como parâmetro.
def fatorial(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return "nao pode ser negativo"
    else:
        return n*fatorial(n-1)

# Exercício 2
# Modele e implemente um método recursivo que calcule o somatório de um número n (passado como parâmetro) até 0.
def somatorio(n):
    if n==0 :
        return 0
    else:
        return n +somatorio(n-1)

# Exercício 3
# Modele e implemente um método recursivo que calcule o n-ésimo número da sequência de fibonacci.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exercício 4
# Modele e implemente um método recursivo que calcule o somatório dos números inteiros entre os números k e j, passados como parâmetro.
def somaint(k,j):
    if j<k:
        return "ordem errada"
    elif j==k+1:
        return 0
    else:
        return j-1 + somaint(k,j-1)


# Exercício 5
# Modele e implemente um método recursivo que recebe um String em retorna true se este String for um palíndrome, false caso contrário.
def palindrome(string):
    string_invertida = string[::-1]
    if strin

string = "Exemplo"
string_invertida = string[::-1]
# Exercício 6

# Exercício 7

# Exercício 8

print(somaint(1,3))