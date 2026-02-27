# ==========================================
# DECISÕES EM PYTHON
# if | elif | else
# operadores de comparação
# operadores lógicos (and / or)
# match (Python 3.10+)
# ==========================================


# -------------------------------
# 1. OPERADORES DE COMPARAÇÃO
# -------------------------------

# val1 == val2  -> igual
# val1 != val2  -> diferente
# val1 >= val2  -> maior ou igual
# val1 <= val2  -> menor ou igual
# val1 < val2   -> menor
# val1 > val2   -> maior

val1 = 4
val2 = 3


# -------------------------------
# 2. IF / ELSE
# -------------------------------
# Verifica se os valores são iguais

if val1 == val2:
    print("Valores iguais")          # executa se a condição for TRUE
else:
    print("Valores diferentes")      # executa se a condição for FALSE


# -------------------------------
# 3. IF / ELIF / ELSE
# -------------------------------
# Verifica qual dos valores é maior

if val1 > val2:
    print("O val1 é maior que val2")
elif val1 == val2:
    print("Valores iguais")
else:
    print("O val2 é maior que val1")


# -------------------------------
# 4. OPERADORES LÓGICOS
# -------------------------------
# and -> ambas as condições têm de ser verdadeiras
# or  -> apenas uma condição tem de ser verdadeira

val3 = 8

# Exemplo com AND
if val1 > val2 and val2 > val3:
    print("val1 é maior e val3 é o menor")

elif val2 > val1 and val1 > val3:
    print("val2 é maior e val3 é o menor")

else:
    print("Nenhuma das condições foi verdadeira")


# -------------------------------
# 5. MATCH (PYTHON 3.10+)
# -------------------------------
# Funciona como um SWITCH

opc = input("1 - Janeiro, 2 - Fevereiro ou 3 - Março: ")

match opc:

    case "1":
        print("Janeiro")

    case "2":
        print("Fevereiro")

    case "3":
        print("Março")

    case _:
        print("Opção não existe")
