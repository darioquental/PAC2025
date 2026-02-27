# ==========================================
# TIPOS DE DADOS EM PYTHON
# string | int | float | bool
# lista | tupla
# ==========================================


# -------------------------------
# 1. STRING (texto)
# -------------------------------

nome = "Joao Carvalho"   # variável do tipo string (texto)

print("Tipo da variável nome:")
print(type(nome))        # mostra o tipo da variável
print("Valor da variável nome:")
print(nome)              # mostra o conteúdo


# -------------------------------
# 2. INT (número inteiro)
# -------------------------------

idade = 32               # número inteiro

print("\nTipo da variável idade:")
print(type(idade))
print("Valor da variável idade:")
print(idade)


# -------------------------------
# 3. FLOAT (número decimal)
# -------------------------------

media = 32.5             # número decimal (float)

print("\nTipo da variável media:")
print(type(media))
print("Valor da variável media:")
print(media)


# -------------------------------
# 4. ALTERAÇÃO DE TIPO
# -------------------------------
# Em Python a variável pode mudar de tipo

media = 32               # agora é inteiro (int)

print("\nTipo da variável media após alteração:")
print(type(media))
print("Novo valor da variável media:")
print(media)


# -------------------------------
# 5. BOOLEAN (True ou False)
# -------------------------------

flag = True              # valor lógico (boolean)

print("\nTipo da variável flag:")
print(type(flag))
print("Valor da variável flag:")
print(flag)


# -------------------------------
# 6. LISTA []
# -------------------------------
# Lista pode guardar vários tipos de dados
# É modificável (podemos alterar valores)

lista = [1, "Dario", 3.4, False]
# índice:  0     1       2     3

print("\nTipo da variável lista:")
print(type(lista))
print("Conteúdo da lista:")
print(lista)

# Acesso ao elemento na posição 2 (terceiro elemento)
print("Elemento na posição 2:")
print(lista[2])


# -------------------------------
# 7. TUPLA ()
# -------------------------------
# Parecida com lista, mas NÃO pode ser alterada (imutável)

nome = "nome1"
idade = "idade1"

tupla = (nome, idade)

print("\nConteúdo da tupla:")
print(tupla)

# Acesso ao elemento na posição 1 (segundo elemento)
print("Elemento na posição 1 da tupla:")
print(tupla[1])


# ==========================================
# FIM DO PROGRAMA
# ==========================================