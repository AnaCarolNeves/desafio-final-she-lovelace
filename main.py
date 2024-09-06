from Registros_vendas import registrar_venda
from Relatorios import gerar_relatorio

def menu(): #Exibe o menu principal e gerencia a escolha do usuário.
    
    while True:
        print("\nSistema de Registro de Vendas")
        print("1. Registrar Venda")
        print("2. Gerar Relatório")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            registrar_venda()
            break
        elif opcao == '2':
            gerar_relatorio()
        elif opcao == '3':
            print("Finalizado")
        else:
            print("Opção inválida. Tente novamente.")   
             
         
        
if __name__ == "__main__":
    menu()                


