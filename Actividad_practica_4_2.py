def primo(n):
    if n%2 != 0:
        return n

lista = [3, 4, 8, 5, 5, 22, 13]

numeros_primos = list(filter(primo, lista))

print(numeros_primos)