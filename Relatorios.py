import pandas as pd
import matplotlib.pyplot as plt
import os

# Nome dado ao arquivo CSV
ARQUIVO_CSV = 'vendas.csv'

def gerar_relatorio():
    # Verificar se o arquivo CSV existe
    if not os.path.exists(ARQUIVO_CSV):
        print(f"Erro: O arquivo {ARQUIVO_CSV} não foi encontrado.")
        return
    
    try:
        # Carregar os dados do CSV em um DataFrame
        df = pd.read_csv(ARQUIVO_CSV, names=['Data', 'Produto', 'Quantidade', 'Preco'])
        
        # Verificar se o DataFrame está vazio
        if df.empty:
            print("Nenhum dado para gerar relatório.")
            return
        
        # Calcular o total de vendas por produto
        df['Total'] = df['Quantidade'] * df['Preco']
        relatorio_produtos = df.groupby('Produto').agg({'Total': 'sum', 'Quantidade': 'sum'}).reset_index()
        
        # Gráfico de Vendas por Produto importada através do Matplotlib
        plt.figure(figsize=(10, 6)) #Cria uma nova figura para o gráfico com o tamanho especificado. O parâmetro figsize define as dimensões da figura (largura, altura).
        plt.bar(relatorio_produtos['Produto'], relatorio_produtos['Total'], color='purple') #Cria o gráfico em barras, definindo os eixos X e Y (sem especificar) e a cor das barras.
        plt.xlabel('Produto') #Define o eixo X como Produto
        plt.ylabel('Total de Vendas (R$)') #Define o eixo Y como Totais de vendas
        plt.title('Vendas Totais por Produto') #Define título
        plt.xticks(rotation=45, ha='right') #Ajusta a aparência dos rótulos no eixo X.
        plt.tight_layout() #Ajusta o layout do gráfico para que tudo se encaixe de maneira adequada, evitando sobreposições e garantindo que os rótulos e títulos sejam exibidos corretamente.
        plt.show() #Exibe o gráfico na tela. Sem esta linha, o gráfico não seria exibido quando executar o script.
        
        print("\nRelatório de Vendas por Produto:")
        print(relatorio_produtos)
        
        # Vendas por data
        relatorio_data = df.groupby('Data').agg({'Total': 'sum', 'Quantidade': 'sum'}).reset_index()
        
        # Gráfico de Vendas por Data importada através do Matplotlib
        plt.figure(figsize=(12, 6))
        plt.plot(relatorio_data['Data'], relatorio_data['Total'], marker='o', linestyle='-', color='orange')
        plt.xlabel('Data')
        plt.ylabel('Total de Vendas (R$)')
        plt.title('Vendas Totais por Data')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        print("\nRelatório de Vendas por Data:")
        print(relatorio_data)

        # Identificação do produto mais vendido
        produto_mais_vendido = df.groupby('Produto').agg({'Quantidade': 'sum'}).reset_index()
        produto_mais_vendido = produto_mais_vendido.sort_values(by='Quantidade', ascending=False).iloc[0]
        
        print("\nProduto Mais Vendido:")
        print(f"Produto: {produto_mais_vendido['Produto']}")
        print(f"Quantidade Vendida: {produto_mais_vendido['Quantidade']}")

        # Gráfico do Produto Mais Vendido importada através do Matplotlib
        plt.figure(figsize=(6, 6))
        plt.pie([produto_mais_vendido['Quantidade']], labels=[produto_mais_vendido['Produto']], autopct='%1.1f%%', colors=['lightcoral'])
        plt.title('Produto Mais Vendido')
        plt.title('Produto Mais Vendido')
        plt.show()

        # Calcular o total geral de vendas
        total_geral = df['Total'].sum()
        print(f"\nTotal Geral de Vendas: R${total_geral:.2f}")
    
    #tratamento de erros (inserido o try na parte de cima do código)
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo CSV está vazio")
    except pd.errors.ParserError:
        print("Erro: Erro ao ler o arquivo CSV. Verifique o formato.")
    except KeyError as e:
        print(f"Erro: Falta de coluna no arquivo CSV - {e}")
    except Exception as e:
        print(f"Erro inesperado ao gerar o relatório: {e}")

