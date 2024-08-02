import time

alunos = []

def timer():
    for _ in range(3):
        print('.\t')
        time.sleep(0.4)
    print()

def dados_A():
    while True:  # Cadastra o nome do aluno
        nome = input("Digite o nome do aluno: ")
        if nome.replace(' ', '').isalpha():
            break
        else:
            print("Nome inválido!")

    while True:  # Cadastra a matricula
        matricula = input("Digite a matrícula do aluno: ")
        if matricula.isdigit() and len(matricula) == 7:
            break
        else:
            print("Matrícula inválida! Deve conter 7 dígitos.")

    while True:  # Cadastra o curso do aluno
        curso = input("Digite o curso do aluno: ")
        if curso.replace(' ', '').isalpha():
            break
        else:
            print("Curso inválido!")
            
    notas_list = []
    while len(notas_list) < 3:  # Insere as notas do aluno
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
    encontrado = False
    for i, aluno in enumerate(alunos):
        if aluno["matricula"] == matricula:
            encontrado = True
            while True:
                opcao = input("1 - Editar Nome.\n2 - Editar Matricula.\n3 - Editar Curso. \n4 - Editar Notas.\n5 - Sair.\n")
                
                if opcao == '1':
                    novo_nome = input("Digite o nome do aluno: ")
                    if novo_nome.replace(' ','').isalpha():
                        alunos[i]["nome"] = novo_nome
                    else:
                        print("Nome inválido, deve conter apenas letras.\n")
                                        
                elif opcao == '2':
                    nova_mat = input("Digite a nova matricula: ")
                    if nova_mat.isdigit() and len(nova_mat) == 7:
                        alunos[i]["matricula"] = nova_mat
                    else:
                        print("Matricula inválida, deve conter 7 dígitos.\n")
                    
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
    if not encontrado:
        print("Matrícula não encontrada.\n")
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

def calcular_media():
    matricula = input("Digite a matrícula do aluno: ")
    encontrado = False
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"A média do(a) aluno(a) {aluno['nome']} é {media:.2f}\n")
            encontrado = True
            break
    if not encontrado:
        print("Matricula não encontrada.\n")
    
print("----- Bem vindo ao sistema de gerenciamento de alunos. -----")
timer()

while True:
    print("1 - Adicionar Alunos.\n2 - Listar Alunos.\n3 - Editar Alunos.\n4 - Excluir Alunos.\n5 - Calcular Media\n6 - Encerrar o programa\n")
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
                print(f"----- Nome: {aluno['nome']}, Matricula: {aluno['matricula']}, Curso: {aluno['curso']}, Notas: {aluno['notas']} -----\n")
    elif escolha == 3:
        edita_A()
        print("Edição Encerrada.\n")
    elif escolha == 4:
        deleta_A()
    elif escolha == 5:
        calcular_media()
    elif escolha == 6:
        print("Programa encerrado")
        break
    else:
        print("Escolha inválida\n")
