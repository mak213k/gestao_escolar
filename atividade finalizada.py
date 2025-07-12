from datetime import date

# Lista de cursos adicionar mais de acordo com os cursos que aparecer so coloquei 7 pq minha criatividade acabou ksksks
cursos = {
    1: {
        'nome': 'Curso de Python',
        'inicio': date(2025, 7, 10),
        'fim': date(2025, 7, 20),
        'fechado': False
    },
    2: {
        'nome': 'Curso de HTML',
        'inicio': date(2025, 7, 1),
        'fim': date(2025, 7, 5),
        'fechado': False
    },
    3: {
        'nome': 'curso de Banco de Dados',
        'inicio': date(2025, 7, 8),
        'fim': date(2025, 9, 7),
        'fechado': False

    },
    4: {
        'nome': 'curso de C++',
        'inicio': date(2025, 8, 10),
        'fim': date(2025, 10, 20),
        'fechado': False
    },
    5:{
        'nome': 'curso de seguranca',
        'inicio': date(2025, 8, 4),
        'fim': date(2025, 10, 6),
        'fechado': False
    },
    6: {
        'nome': 'curso de Seguranca no Trabalho',
        'inicio': date(2025, 8, 5),
        'fim': date(2025, 9, 7),
        'fechado': False

    },
    7: {
        'nome': 'curso de redes',
        'inicio': date(2025, 9, 10),
        'fim': date(2025, 9, 8),
        'fechado': False
    }

}

# Funcao para verificar o status
def verificar_status(curso_id):
    hoje = date.today()

    if curso_id in cursos:
        curso = cursos[curso_id]

        if curso['fechado']:
            print(f"O curso '{curso['nome']}' esta FECHADO .")
        elif curso['inicio'] <= hoje <= curso['fim']:
            print(f"O curso '{curso['nome']}' esta ABERTO!")
        else:
            print(f"O curso '{curso['nome']}' esta FECHADO (fora do periodo).")
    else:
        print("Curso nao encontrado.")

# Funcao para fechar o curso
def fechar_curso(curso_id):
    if curso_id in cursos:
        cursos[curso_id]['fechado'] = True
        print(f"O curso '{cursos[curso_id]['nome']}' foi FECHADO manualmente.")
    else:
        print("Curso nao encontrado.")

# Menu
while True:
    print("\n--- MENU ---")
    print("1 - Ver status de um curso")
    print("2 - Fechar um curso")
    print("3 - Sair")
    
    opcao = input("Escolha uma opcao: ")

    if opcao == '1':
        curso_id = int(input("Digite o numero do curso: "))
        verificar_status(curso_id)

    elif opcao == '2':
        curso_id = int(input("Digite o numero do curso que deseja fechar: "))
        fechar_curso(curso_id)

    elif opcao == '3':
        print("Saindo...")
        break

    else:
        print("Opcao invalida.")