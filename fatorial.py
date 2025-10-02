number = int(input("Digite um valor para descobrir o seu fatorial: "))
fatorial = 1

for i in range(1, number+1):
    fatorial *= i

print(f"O fatorial de {number} é {fatorial}")
