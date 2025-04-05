print ("-------Sistema de um Hotel-------")
print ("\n")



cliente1=input("Digite seu nome: ")
idade1=int(input(f"Digite sua idade sr(a) {cliente1} : "))
cliente2=input("Digite seu nome: ")
idade2=int(input(f"Digite sua idade sr(a) {cliente2} : "))
cliente3=input("Digite seu nome: ")
idade3=int(input(f"Digite sua idade sr(a) {cliente3} :  "))


quarto=["Simples","Duplo","Luxo"]
preco=[100,150,250]



print("Quartos Disponiveis: \n ---Simples--- \n ---Duplo--- \n ---Luxo---")
q1=input(f"Escolha um tipo de quarto sr(a) {cliente1} :   ")
q2=input(f"Escolha um tipo de quarto sr(a) {cliente2} :   ")
q3=input(f"Escolha um tipo de quarto sr(a) {cliente3} :   ")



if q1==quarto[0]:     
    print(f"\n---Você escolheu o quarto simples sr(a) {cliente1} !!---")
    diaria=int(input("\nEscolha quantos dias deseja ficar: "))
    valor_cliente1 = preco[0] * diaria
    print(f"O valor da sua diaria sr(a) {cliente1} é de : R${valor_cliente1} ")
if q2==quarto[0]:
        print(f"\n---Você escolheu o quarto simples sr(a) {cliente2}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente2 = preco[0] * diaria
        print(f"O valor da sua diaria sr(a) {cliente2} é de : R${valor_cliente2} ") 
if q3==quarto[0]:
        print(f"\n---Você escolheu o quarto simples sr(a) {cliente3}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente3 = preco[0] * diaria
        print(f"\nO valor da sua diaria sr(a) {cliente3} é de : R${valor_cliente3} ")

if q1==quarto[1]:     
    print(f"\n---Você escolheu o quarto duplo sr(a) {cliente1} !!---")
    diaria=int(input("\nEscolha quantos dias deseja ficar: "))
    valor_cliente1 = preco[1] * diaria
    print(f"O valor da sua diaria sr(a) {cliente1} é de : R${valor_cliente1} ")
if q2==quarto[1]:
        print(f"\n---Você escolheu o quarto duplo sr(a) {cliente2}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente2 = preco[1] * diaria
        print(f"O valor da sua diaria sr(a) {cliente2} é de : R${valor_cliente2} ") 
if q3==quarto[1]:
        print(f"\n---Você escolheu o quarto duplo sr(a) {cliente3}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente3 = preco[1] * diaria
        print(f"\nO valor da sua diaria sr(a) {cliente3} é de : R${valor_cliente3} ")

if q1==quarto[2]:     
    print(f"\n---Você escolheu o quarto luxo sr(a) {cliente1} !!---")
    diaria=int(input("\nEscolha quantos dias deseja ficar: "))
    valor_cliente1 = preco[2] * diaria
    print(f"O valor da sua diaria sr(a) {cliente1} é de : R${valor_cliente1} ")
if q2==quarto[2]:
        print(f"\n---Você escolheu o quarto luxo sr(a) {cliente2}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente2 = preco[2] * diaria
        print(f"O valor da sua diaria sr(a) {cliente2} é de : R${valor_cliente2} ") 
if q3==quarto[2]:
        print(f"\n---Você escolheu o quarto luxo sr(a) {cliente3}!!---")
        diaria=int(input("\nEscolha quantos dias deseja ficar: "))
        valor_cliente3 = preco[2] * diaria
        print(f"\nO valor da sua diaria sr(a) {cliente3} é de : R${valor_cliente3} ")


elif q1!=quarto and q2!=quarto and q3!=quarto:

    print("Informações invalidas, tente novamente")