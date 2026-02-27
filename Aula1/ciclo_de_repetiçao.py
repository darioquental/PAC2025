# ==========================================
# REPETIÇÃO DE AÇÕES EM PYTHON
# while | for (tipo foreach)
# listas | break | continue
# ==========================================


# -------------------------------
# 1. CRIAR UMA LISTA
# -------------------------------

# Criar uma lista de números
lista = [1, 2, 34, 5, 6, 7, 7, 8]

# Mostrar o tamanho da lista
# len() devolve o número de elementos da lista
print("Tamanho da lista:")
print(len(lista))


# -------------------------------
# 2. CICLO WHILE
# -------------------------------
# Repete enquanto a condição for verdadeira

print("\nExemplo de WHILE:")

while True:  # ciclo infinito até o utilizador parar
    
    # pedir valor ao utilizador
    parar = int(input("Digite 1 para parar: "))
    
    # se o utilizador digitar 1
    if parar == 1:
        break   # sai imediatamente do ciclo
    
    print("O programa continua...")


# -------------------------------
# 3. BREAK E CONTINUE
# -------------------------------

print("\nExemplo de CONTINUE:")

i = 0

# repete enquanto i for menor que 5
while i < 5:
    
    i += 1   # incrementa 1 ao i
    
    # quando i for igual a 3
    if i == 3:
        continue   # ignora o resto do código e volta ao início
    
    print(i)   # o número 3 não será mostrado


# -------------------------------
# 4. CICLO FOR COM ÍNDICE
# -------------------------------
# Usado quando precisamos da posição do elemento

print("\nPercorrer lista com FOR (índice):")

for j in range(len(lista)):
    
    # range(len(lista)) cria números de 0 até ao tamanho da lista
    # j representa a posição (índice)
    
    print(lista[j])   # mostra cada elemento da lista


# -------------------------------
# 5. CICLO FOR (TIPO FOREACH)
# -------------------------------
# Percorre automaticamente todos os elementos
# Sem usar índice

print("\nPercorrer lista com FOR (tipo foreach):")

for elemento in lista:
    
    # "elemento" recebe automaticamente cada valor da lista
    print(elemento)
