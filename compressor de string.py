def comprimir_string(s):
    if not s:
        return ""
    
    contagem_atual = 1
    string_comprimida = []
    
   
    for i in range(1, len(s)):
        
        if s[i] == s[i-1]:
            contagem_atual += 1
        else:
            
            string_comprimida.append(str(contagem_atual) + s[i-1])
           
            contagem_atual = 1
    
    
    string_comprimida.append(str(contagem_atual) + s[-1])
    
    
    resultado = ''.join(string_comprimida)
    

    return resultado if len(resultado) < len(s) else s

print(comprimir_string("aaabbbcccc"))  # Saída: "3a3b4c"
print(comprimir_string("abcde"))       # Saída: "abcde"
print(comprimir_string("aabcccccaaa")) # Saída: "2a1b5c3a"