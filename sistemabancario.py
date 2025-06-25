menu = """

[1] Depositar
[2] Sacar 
[3] Extrato 
[4] Sairc

=> """

saldo= 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    opcao = input(menu)
    
    if opcao == "1" :
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito : R$ {valor: .2f}\n"
        else: print("Operação falhou: O valor informado é inválido.")
    elif opcao == "2":
        valor= float(input("Informe o valor do saque: "))

        execedeu_saldo= valor > saldo
        
        execedeu_limite = valor > limite 
        
        execedeu_saques= numero_saques >= LIMITE_SAQUES
        
        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
           
        elif execedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite.")
        
        elif execedeu_saques: 
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R${valor: .2f}\n"
             numero_saques += 1
             
        else: 
            print("operação falhou! O valor informado é inválido. ")
    
    elif opcao == "3":
        print ("\n =============EXTRATO==========")
        print ("Não foram realizadas movimentações." if not  extrato else extrato)
        print (f"\n saldo: R$ {saldo: .2f}")
        print ("######################################")
         
    elif opcao == "4":
        break
    
    else: 
        print ("Operação inválida, por favor selecione novamnete a operação desejada.")
                 