import csv
from tabulate import tabulate

def ler_csv(caminho_arquivo):
    try:
    
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            
            leitor_csv = csv.reader(arquivo)
            
            cabecalho = next(leitor_csv, None)
            
            linhas = list(leitor_csv)
            
            if cabecalho and linhas:
                print(tabulate(linhas, headers=cabecalho, tablefmt='grid'))
            else:
                print("O arquivo CSV está vazio.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except csv.Error as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def main():

    caminho_arquivo = input("Digite o caminho do arquivo CSV: ")
    
    ler_csv(caminho_arquivo)

if __name__ == "__main__":
    main()