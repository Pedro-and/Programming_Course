import time

class Aluno:
    def __init__(self, nome, matricula, curso, notas):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Nome: {self.nome}\n Matricula: {self.matricula}\n Curso: {self.curso}\n Notas: {self.notas}"

class GerenciamentoAlunos:
    def __init__(self):
        self.alunos = []

    def timer(self):
        for _ in range(3):
            print('.\t')
            time.sleep(0.4)
        print()

    def adicionar_aluno(self):
        while True:
            nome = input("Digite o nome do aluno: ")
            if nome.replace(' ', '').isalpha():
                break
            else:
                print("Nome inválido!")

        while True:
            matricula = input("Digite a matrícula do aluno: ")
            if matricula.isdigit() and len(matricula) == 7:
                break
            else:
                print("Matrícula inválida! Deve conter 7 dígitos.")

        while True:
            curso = input("Digite o curso do aluno: ")
            if curso.replace(' ', '').isalpha():
                break
            else:
                print("Curso inválido!")

        notas_list = []
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

        aluno = Aluno(nome, matricula, curso, notas_list)
        self.alunos.append(aluno)
        print("Aluno cadastrado com sucesso!\n")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.\n")
        else:
            for aluno in self.alunos:
                print(f"{aluno}\n")

    def editar_aluno(self):
        matricula = input("Digite a matricula do aluno: ")
        encontrado = False
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                encontrado = True
                while True:
                    opcao = input("1 - Editar Nome.\n2 - Editar Matricula.\n3 - Editar Curso. \n4 - Editar Notas.\n5 - Sair.\n")
                    
                    if opcao == '1':
                        novo_nome = input("Digite o nome do aluno: ")
                        if novo_nome.replace(' ', '').isalpha():
                            aluno.nome = novo_nome
                        else:
                            print("Nome inválido, deve conter apenas letras.\n")
                                        
                    elif opcao == '2':
                        nova_mat = input("Digite a nova matricula: ")
                        if nova_mat.isdigit() and len(nova_mat) == 7:
                            aluno.matricula = nova_mat
                        else:
                            print("Matricula inválida, deve conter 7 dígitos.\n")
                    
                    elif opcao == '3':
                        novo_curso = input("Digite o novo curso: ")
                        if novo_curso.replace(' ', '').isalpha():
                            aluno.curso = novo_curso
                        else:
                            print("Curso inválido, digite apenas letras")
                         
                    elif opcao == '4':
                        novas_notas = []
                        while len(novas_notas) < 3:
                            try:
                                nova_nota = float(input("Digite as novas notas: "))
                                if 0 <= nova_nota <= 10:
                                    novas_notas.append(nova_nota)
                                else:
                                    print("A nota tem que estar entre 0 e 10.")
                            except ValueError:
                                print("Nota inválida. Por favor, insira um número.")
                        aluno.notas = novas_notas
                        print("Notas atualizadas com sucesso!")

                    elif opcao == '5':
                        break
                print("Edição Encerrada.\n")
                break
        if not encontrado:
            print("Matrícula não encontrada.\n")

    def deletar_aluno(self):
        matricula = input("Digite a matrícula do aluno que deseja excluir: ")
        encontrado = False
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                print("Aluno removido com sucesso!\n")
                encontrado = True
                break
        
        if not encontrado:
            print("Matrícula não encontrada.\n")

    def calcular_media_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        encontrado = False
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                media = aluno.calcular_media()
                print(f"A média do(a) aluno(a) {aluno.nome} é {media:.2f}\n")
                encontrado = True
                break
        if not encontrado:
            print("Matricula não encontrada.\n")

class menu():
    sistema = GerenciamentoAlunos()
    print("----- Bem vindo ao sistema de gerenciamento de alunos -----")
    sistema.timer()

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
            sistema.timer()
            sistema.adicionar_aluno()
            
        elif escolha == 2:
            print("Opção 2 selecionada.\n")
            sistema.timer()
            sistema.listar_alunos()
            
        elif escolha == 3:
            sistema.editar_aluno()
            
        elif escolha == 4:
            sistema.deletar_aluno()
            
        elif escolha == 5:
            sistema.calcular_media_aluno()
            
        elif escolha == 6:
            print("Programa encerrado")
            break
        
        else:
            print("Escolha inválida\n")
