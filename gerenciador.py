import time
alunos = []

def timer():
    
    for _ in range(3):
        
        print('.\t')
        time.sleep(0.4)

def dados_A():
    
    while True:         #Cadastra o nome do aluno, a função replace serve para tirar espaços usados por acidente. funciona por exemplo ('old','new').
        nome = input("Digite o nome do aluno: ")
        if nome.replace(' ', '').isalpha():  
            break
        else:
            print("Nome inválido!")
            
    while True:         #Cadastra a matricula, permite apenas números e a matricula PRECISA ter 7 dígitos.  .isdigit() permite apenas números.
        matricula = input("Digite a matrícula do aluno: ")          
        if matricula.isdigit() and len(matricula) == 7: 
            break
        else:
            print("Matrícula inválida! Deve conter 7 dígitos.")
    
    while True:         #Cadastra o curso do aluno, .isalpha() usado anteriormente serve para permitir apenas letras.
        curso = input("Digite o curso do aluno: ")
        if curso.replace(' ', '').isalpha(): 
            break
        else:
            print("Curso inválido!")
    
    notas_list = []
    
    while True:        #Insere as notas do aluno, verifica se o decimal foi inserido com ponto (usando o try except) e se não há letras nas notas.
        while len(notas_list) < 3:
            nota_str = input("Digite a(s) nota(s) do aluno (ou f para finalizar.): ")
            if nota_str.lower() == 'f':                   
                break
            try:
                nota = float(nota_str)
                if 0 <= nota <= 10:
                    notas_list.append(nota)
                else:
                    print("A nota não pode ser menor que zero e maior que dez.")
            except ValueError:
                print("Nota inválida! Digite um número válido.")
        
        return {'nome': nome, 'matricula': matricula, 'curso': curso, 'notas': notas_list}
    
def edita_A():
    
    notas_novas = []
    
    matricula = input("Digite a matricula do aluno: ")
    for i, aluno in enumerate (alunos):
        if aluno["matricula"] == matricula:
            while True:
                opcao = input("1 - Editar Nome.\n2 - Editar Matricula.\n3 - Editar Curso. \n4 - Editar Notas.\n5 - Sair.\n")
                
                if opcao == '1':
                    novo_nome = input("Digite o nome do aluno: ")
                    if novo_nome.replace(' ','').isalpha():
                        alunos[i]["nome"] = novo_nome
                    else:
                        print("Nome invalido, deve conter apenas letras.\n")  
                                        
                elif opcao == '2':
                        nova_mat = input("Digite a nova matricula: ")
                        if nova_mat.isdigit() and len(nova_mat) == 7:
                            alunos[i]["matricula"] = nova_mat
                        else:
                            print("Matricula invalida, deve conter 7 digitos.\n")
                    
                elif opcao == '3':
                     novo_curso = input("Digite o novo curso: ")
                     if novo_curso.replace(' ','').isalpha():
                        alunos[i]["curso"] = novo_curso
                     else:
                         print("Curso inválido, digite apenas letras")
                         
                elif opcao == '4':
                    notas_novas = []
                    
                    while len(notas_novas) < 3:
                            try:
                                novas_notas = float(input("Digite as novas notas: "))
                                if 0 <= novas_notas <= 10:
                                    notas_novas.append(novas_notas)
                                else:
                                    print("A nota tem que estar entre 0 e 10.")
                            except ValueError:
                                print("Nota inválida. Por favor, insira um número.")
                        
                    alunos[i]["notas"] = notas_novas
                    print("Notas atualizadas com sucesso!")

                elif opcao == '5':
                    break
    return alunos

def deleta_A():
    matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    encontrado = False
    for i in range(len(alunos)):
        if alunos[i]["matricula"] == matricula:
            del alunos[i]
            print("Aluno removido com sucesso!\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Matrícula não encontrada.\n")
    
    return alunos
    
    
    
print("|---------------------------------------------------------------------------------|")
print("| Bem vindo ao sistema de gerenciamento de alunos. Pressione Enter para prosseguir|")
print("|_________________________________________________________________________________|")
timer()

while True:
    print("1 - Adicionar Alunos.\n2 - Listar Alunos.\n3 - Editar Alunos.\n4 - Excluir Alunos.\n")
    escolha = input("Escolha uma opção: ").strip()
    print()
    
    if not escolha.isdigit():
        print("Digite apenas o número da opção desejada.")
        continue
    escolha = int(escolha)
    if escolha == 1:
        print("Opção 1 selecionada.\n")
        timer()
        aluno = dados_A()
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!\n")
    elif escolha == 2:
        print("Opção 2 selecionada.\n")
        timer()
        if not alunos:
            print("Nenhum aluno cadastrado.\n")
        else:
            for aluno in alunos:
                print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}, Curso: {aluno['curso']}, Notas: {aluno['notas']}\n")
    elif escolha == 3:
        alunos = edita_A()
        if alunos in alunos:
            print("Aluno editado com sucesso!")
        else:
            print("Aluno não encontrado.\n")
    elif escolha == 4:
        aluno_excluido = deleta_A()
    
    