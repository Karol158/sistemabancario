import os
from datetime import date,datetime
nome = []
cpf =[]
numeroconta =[]
saldo =[]
historico=[]

data= date.today()
print(data)
hora = datetime.now()
print("Hora atual:", hora.strftime("%H:%M:%S"))
def limpar():
    os.system("cls")   
def criarconta():
    limpar()
    nome.append(input("seu nome:"))
    cpf.append(input("seu cpf:"))
    saldo.append(0)
    numeroconta.append(input("o numero da conta:"))
    limpar()
    menu() 
        
def alterar():
    limpar()
    print("Digite o numero da conta que você quer alterar")
    print("alterarcpf:'1'\n alterarnome:'2'")
    conta = input("Digite o numero da conta:")
    encontrado = False
    
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Esta conta não existe")
    if conta == numeroconta[i]:
        pedido=input("O que voce deseja alterar")
    if pedido == '1':
        cpf[i] = input("Digite seu cpf novo:") 
    elif pedido == '2': 
        nome[i] = input("Digite seu novo nome:") 
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  

def consultar():
    limpar()
    conta = input("O número da sua conta: ")
    encontrado = False
    for i in range(len(numeroconta)):
        if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    if not encontrado:
        print("conta não existe")
       
    voltar =input("Digite 'sair' pra voltar pro inicio")
    if voltar=='sair':
     limpar()
     menu() 

def excluirconta():
    limpar()
    print("Digite o numero da conta para exclui-lá")
    conta=input("digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
           print("essa conta não existe")
    
    if conta==numeroconta[i]:
          pedido=input("Voce quer excluir conta?")
    if pedido=="sim":     
          del(cpf[i])
          del(nome[i])
          del(numeroconta[i])
          del(saldo[i])
          print("conta excluída")
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()  
def depositar():
    limpar()
    valor=int(input("digite o valor a ser depositado:"))
    conta=input("Digite o numero da conta:")
    encontrado = False
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
    if not encontrado:
           print("conta não encontrada")
    
    if conta == numeroconta[i]:
         saldo[i]=saldo[i]+valor
         historico.append(f"Você recebeu um valor de: {valor},hora:{hora.strftime("%H:%M:%S")} ")
    inicio = input("Digite 'sair' para voltar para o início: ")
    if inicio == 'sair':
        limpar()
        menu()
def pix():
     limpar()
     print("Digite o numero da conta para fazer o pix")
     valor=int(input("Qual o valor a transferir?"))
     conta=input("Digite o numero da conta")
     encontrado = False
     for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
            print(f"Conta: {numeroconta[i]}\nCPF: {cpf[i]}\nNome: {nome[i]}\nSaldo: {saldo[i]}")
            encontrado = True
            break
    
     if not encontrado:
           print("conta não encontrada")
    
     if conta == numeroconta[i]:
         saldo[i]=saldo[i]-valor
     historico.append(f"Você fez um pix de:{valor},no dia:{data},hora:{hora.strftime("%H:%M:%S")} ")
     print("Pix realizado")
     saida = input("Digite 'sair' para voltar para o início: ")
     if saida == 'sair':
        limpar()
        menu()
def histórico():
    limpar()
    print("Digite o numero da conta para ver o seu historico")
    conta=input("Digite o numero da conta")
    for i in range(len(numeroconta)):
         if numeroconta[i] == conta:
             print(historico)
         else:
             print("Essa conta não existe")
    saida = input("Digite 'sair' para voltar para o início: ")
    if saida == 'sair':
           limpar()
           menu()
    

def menu():
    print("*****sistema bancário*******")
    print("\n \n criar conta: '1'\n alterar conta:'2' \n consultar conta:'3'\n excluir conta:'4' \n depositar'5'\n fazer pix:'6'\n Ver meus histórico:'7' ")
    x = input("o que voce quer fazer?")
    
    if x == '1':
      limpar()
      criarconta()

    elif x == '3':
     limpar()
     consultar()
     
    elif x =='2':
       limpar()
       alterar()

    elif x=='4':
       limpar()
       excluirconta()
    elif x=='7':
        limpar()
        depositar()

    elif x=='8':
        limpar()
        pix()
    elif x=='9':
        limpar()
        histórico()

menu()