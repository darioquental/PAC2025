# if e match(py v10)

# operadores de decisão 
# 
# val1 == val2
# val1 != val2
# val1 >= val2
# val1 <= val2
# val1 < val2
# val1 > val2

val1=4
val2=3

if val1 == val2:
    print("valores iguais")      # if val1 == val2 true
else:
    print("valores diferentes")   # if val1 == val2 false


if val1 > val2:
    print(" o val1 é maior que val2 ")
elif val1 == val2:
    print("valores iguais") 
else:
    print(" o val2 é maior que val1 ")


#       Val1 > Val2   Operador Logico   Val2 > Val3
# and   &&
# or    ||

val3=8

if val1 > val2 and val2 > val3:
     print(" o val1 é maior e val3 é o menor ")
elif  val2 > val1 and val1 > val3:
      print(" o val2 é maior e val3 é o menor ")



opc=input("1- Janeiro , 2 - fevereiro ou 3 março")


match opc :
    case "1":
        print("Janeiro")
    case "2":
        print("fevereiro")
    case "3":
        print("março")
    case _:
         print("opçao nao existe")