#funçao de adiçao
def add(a, b):
    answer = a + b
    print (str(a) + " + " + str(b) + " = " + str(answer) + "\n")
#funçao de subtraçao 
def sub(a, b):
    answer = a - b
    print (str(a) + " - " + str(b) + " = " + str(answer) + "\n")
#funçao de multiplicaçao
def mul(a, b):
    answer = a * b
    print (str(a) + " * " + str(b) + " = " + str(answer) + "\n")
#funçao de divisao
def div(a, b):
    answer = a / b
    print (str(a) + " / " + str(b) + " = " + str(answer) + "\n")
 
while True: 

    print("A. Addiction")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")


    choice = input("Input your choice: ")
#verifica de a escolha foi o caracter da adiçao
    if choice == "a" or choice == "A":
        print("Addiction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        #adiciona os numeros 
        add(a, b)
#verifica de a escolha foi o caracter da subtracao
    elif choice == "b" or choice == "B": 
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        #subtrai os numeros 
        sub(a, b)
#verifica de a escolha foi o caracter da multiplicaçao
    elif choice == "c" or choice == "C": 
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        #multiplica os numeros 
        mul(a, b)  
#verifica de a escolha foi o caracter da divisao 
    elif choice == "d" or choice == "D": 
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        #divide os numeros 
        div(a, b)
#verifica de a escolha foi o caracter da saida do programa
    elif choice == "e" or choice == "E":
        print("Program ended")
        #termina o programa 
        quit()