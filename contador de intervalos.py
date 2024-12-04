def contador_intervalos():

    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0
    
    while True:
        try:

            numero = float(input("Digite um numero (negativo para sair): "))
            
            
            if numero < 0:
                break
            
            if 0 <= numero <= 25:
                intervalo_0_25 += 1
            elif 26 <= numero <= 50:
                intervalo_26_50 += 1
            elif 51 <= numero <= 75:
                intervalo_51_75 += 1
            elif 76 <= numero <= 100:
                intervalo_76_100 += 1
        
        except ValueError:
        
            print("Entrada invalida. Digite um numero valido.")
    
    
    print("\nRelatório de Intervalos:")
    print(f"Numeros no intervalo [0-25]:   {intervalo_0_25}")
    print(f"Numeros no intervalo [26-50]:  {intervalo_26_50}")
    print(f"Numeros no intervalo [51-75]:  {intervalo_51_75}")
    print(f"Numeros no intervalo [76-100]: {intervalo_76_100}")


def main():
    print("Contador de Intervalos")
    print("Digite numeros entre 0 e 100. Digite um numero negativo para encerrar.")
    contador_intervalos()

if __name__ == "__main__":
    main()