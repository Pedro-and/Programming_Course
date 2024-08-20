import yfinance
import time
import webbrowser
import pyautogui

print(" ---- Bem-vindo ao consultador de ações! ----\n\n")
ticker = input("Digite a ação que deseja consultar: ").upper()

def data_i():
    ano_i = input("Digite o ano inicial da consulta (YYYY): ")
    mes_i = input("Digite o mês inicial da consulta (MM): ")
    dia_i = input("Digite o dia inicial da consulta (DD): ")
    print()
    return f"{ano_i.zfill(4)}-{mes_i.zfill(2)}-{dia_i.zfill(2)}"

def data_f():
    ano_f = input("Digite o ano final da consulta (YYYY): ")
    mes_f = input("Digite o mês final da consulta (MM): ")
    dia_f = input("Digite o dia final da consulta (DD): ")
    print()
    return f"{ano_f.zfill(4)}-{mes_f.zfill(2)}-{dia_f.zfill(2)}"

def obter_dados(ticker, inicio, final):
    return yfinance.Ticker(ticker).history(start=inicio, end=final)

def maxima_minima_media(dados, coluna):
    print(f"Você escolheu: Máxima, mínima ou média da {coluna}\n")
    escolha = input("Deseja enviar a máxima, mínima ou média? ").lower()
    if escolha == "maxima":
        resultado = dados[coluna].max()
    elif escolha == "minima":
        resultado = dados[coluna].min()
    elif escolha == "media":
        resultado = dados[coluna].mean()
    else:
        print("Opção inválida.")
        return None
    return resultado

def sair():
    print("Saindo...")
    exit()

inicio = data_i()
final = data_f()
dados = obter_dados(ticker, inicio, final)

while True:
    print("Escolha o dado a ser acessado.\n")
    escolha = int(input("1 - Todos os dados\n2 - Abertura\n3- Fechamento\n4 - Alta\n5 - Baixa\n6 - Volume\n7 - Sair\n\n"))

    if escolha == 1:
        print()
        time.sleep(0.5)
        print(f"Segue todos os dados abaixo: \n\n{dados}\n")
    elif escolha == 2:
        print()
        print(f"Segue a abertura abaixo: \n\n{dados['Open']}\n")
    elif escolha == 3:
        print()
        print(f"Segue o fechamento abaixo: \n\n{dados['Close']}\n")
    elif escolha == 4:
        print()
        print(f"Segue a alta abaixo: \n\n{dados['High']}\n")
    elif escolha == 5:
        print()
        print(f"Segue a baixa abaixo: \n\n{dados['Low']}\n")
    elif escolha == 6:
        print()
        print(f"Segue o volume abaixo: \n\n{dados['Volume']}\n")
    elif escolha == 7:
        sair()
    else:
        print("Escolha inválida, tente novamente.\n")
        continue  

    
    escolha_email = input("Deseja enviar por e-mail? Y/n ").upper()
    if escolha_email == "Y":
        destinatario = input("Digite o e-mail do destinatário: ")

        opcoes = {
            1: 'Close',   
            2: 'Open',   
            3: 'High',    
            4: 'Low',     
            5: 'Volume'  
        }

        print("O que deseja enviar no relatório?\n")
        try:
            relatorio = int(input("1 - Fechamento\n2 - Abertura\n3 - Alta\n4 - Baixa\n5 - Volume\n6 - Sair\n"))
            if relatorio in opcoes:
                resultado = maxima_minima_media(dados, opcoes[relatorio])
                if resultado is not None:
                    print(f"O resultado da {opcoes[relatorio]} é: {resultado}\n")
                    
                    assunto = f"Análise de dados da empresa {ticker} referente ao periodo de {inicio} - {final}"
                    mensagem = f"""
                    Prezado gestor,

                    Segue a analise do dado da empresa {ticker}:

                    A {opcoes[relatorio]} da empresa {ticker} foi de R$ {round(resultado, 2)} no periodo de {inicio} a {final}.

                    Atenciosamente,
                    [Seu Nome]
                    """

                    webbrowser.open("https://mail.google.com")      #Coordenadas podem mudar de acordo com o monitor
                    
                    time.sleep(3)
                    pyautogui.PAUSE = 2
                    pyautogui.click(x=117, y=203)

                    pyautogui.write(destinatario)
                    pyautogui.hotkey("enter")
                    pyautogui.hotkey("tab")

                    pyautogui.write(assunto)
                    pyautogui.hotkey("tab")

                    pyautogui.write(mensagem)
                    pyautogui.click(x=1301, y=997)
                else:
                    print("Nenhum dado válido para o relatório.")
            elif relatorio == 6:
                sair()
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

    
    repetir = input("Deseja consultar os dados novamente? Y/n ").upper()
    if repetir != "Y":
        break

print("Obrigado por usar meu programa, até a próxima!")
