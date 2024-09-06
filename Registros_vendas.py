import csv
from datetime import datetime #importada para registrar a data e hora de venda

ARQUIVO_CSV = 'vendas.csv'

def registrar_venda():
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #define formato da hora e data
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade vendida: "))
    preco = float(input("Digite o preço unitário: "))
    
    try: 
        with open(ARQUIVO_CSV, mode='a') as arquivo: #mode='a' significa "append" (acrescentar). Os dados serão adicionados ao final do arquivo sem sobrescrevê-lo.
            writer = csv.writer(arquivo)
            writer.writerow([data, produto, quantidade, preco])
        print("Venda registrada com sucesso!")
    except IOError as e:
            print(f"Erro ao abrir o arquivo CSV: {e}")
    except Exception as e:
            print(f"Erro ao registrar a venda: {e}")
'''def main():
    print("Sistema de Registro de Vendas")
    
    try:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #define formato da hora e data
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade vendida: "))
        preco = float(input("Digite o preço unitário: "))
        
        if quantidade <= 0 or preco <= 0:
            raise ValueError("Quantidade e preço devem ser positivos.")
        
        registrar_venda(data, produto, quantidade, preco)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")'''''
        
       
#if __name__ == "__main__":
    #main()