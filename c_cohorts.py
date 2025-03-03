from b_courses import courses, print_courses
from f_students import print_students_wo_cohort, students
from g_util import code_existance_verifier, code_verifier_index

cohorts = []

def registering_cohorts():
    """registering_cohorts: Função Principal da criação de Turmas

    Chama as funções necessárias para que o usuário possa inserir os dados necessários
    para a criação de uma nova turma em formato de dicionário para ser inserida na lista cohorts
    """
    print('\nOs cursos cadastrados são:')
    print_courses()
    exists = False
    while not exists:
        user_code = input(f'Insira o Código do Curso do qual essa Turma fará parte: ').upper()
        exists, course_name = code_existance_verifier(user_code, courses)
        if not exists:
            print('\nCódigo inválido, tente novamente.')
    year = rec_cohort_year()
    semester = rec_cohort_semester()
    name = create_cohort_name(course_name, year, semester)
    code = create_cohort_code(user_code, year, semester)
    cohorts.append(create_cohort_dict(name, code))
    
def rec_cohort_year():
    """rec_cohort_year: Receber o Ano da turma sendo cadastrada.

    Recebe o Ano e verifica se é válido para a turma. Por definição, permiti
    a criação apenas de turmas dos anos 2020 a 2025. Enquanto não inserir um ano
    válido, a função continuará solicitando um Ano válido.

    Returns:
        year str: O ano da turma em questão, que será, em outra função, concatenado para gerar o Nome da turma.
    """
    year_available = ["20", "21", "22", "23", "24", "25"]
    while True:
            year = str(input(f'\nOs Anos disponíveis são: 2020, 2021, 2022, 2023, 2024 e 2025\nInsira o Ano dessa Turma: '))
            year = year[-2:]
            if year in year_available:
                return year
            print('\nErro! Ano inválido. Tente novamente.')

def rec_cohort_semester():
    """rec_cohort_semester: Receber o Semestre da turma sendo cadastrada.

    Recebe o Semestre e verifica se é válido, ou seja, "1" ou "2".
    Enquanto não inserir um valor válido, a função continuará solicitando um Semestre válido.

    Returns:
        semester str: Uma string "1" ou "2" para, posteriormente, ser concatenada no Nome da turma.
    """
    while True:
        semester = str(input('\nInsira o Semestre dessa Turma ("1" ou "2"): ')).strip("'").strip('"')
        if semester in ('1', '2'):
            return semester
        print('\nErro! Valor inválido para Semestre. Tente novamente.')

def create_cohort_name(course_name, cohort_year, cohort_semester):
    """create_cohort_name: Cria o Nome da Turma

    Quando é chamada, tem a função de retornar o Nome da turma sendo criada

    Args:
        course_name str: Nome do curso gerador da turma
        cohort_year str: Ano da turma
        cohort_semester str: Semestre da turma

    Returns:
        cohort_name str: Nome da Turma que está sendo criada
    """
    cohort_name = f'{course_name} {cohort_year}{cohort_semester}'
    return cohort_name

def create_cohort_code(course_code, cohort_year, cohort_semester):
    """create_cohort_code: Criar o Código da Turma

    Quando é chamada, tem a função de retornar o Código da turma sendo criada

    Args:
        course_code str: Código do curso gerador da turma (Formato X####, onde X representa Letra Maiúscula e # representa número inteiro entre 0 e 9)
        cohort_year str: Ano da turma
        cohort_semester str: Semestre da turma

    Returns:
        cohort_code str: Código da turma = Código do Curso+AAS, onde "AA" é o Ano da turma, e "S" é o Semestre da turma.
    """
    cohort_code = f'{course_code}{cohort_year}{cohort_semester}'
    return cohort_code

def create_cohort_dict(cohort_name, cohort_code):
    """create_cohort_dict: Criar o dicionário da Turma

    Com os dados necessários, cria o Dicionário original da Turma, composto por Nome e Código únicos.

    Args:
        cohort_name str: Nome da Turma
        cohort_code str: Código da Turma

    Returns:
        Dicionário da Turma dict: Dicionário original da Turma, composto por Nome e Código únicos.
    """
    return {'Nome': cohort_name, 'Código': cohort_code, 'Disciplinas': [], 'Alunos': []}

def print_cohorts(keys_to_display):
    """print_cohorts: Exibe todas as Turmas cadastradas e seus Items selecionados.

    Exibe todas as Turmas cadastradas e seus Items selecionados via argumento.

    Args:
        keys_to_display tuple: Tupla contendo as chaves, cujos items deverão ser exibidos.
    """
    print('\nEstas são as Turmas cadastradas:')
    for cohort in sorted(cohorts, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {cohort[key]}' for key in keys_to_display if key in cohort]))

def print_cohorts_with_workload(keys_to_display):
    """print_cohorts_with_workload: Exibe todas as Turmas e os itens selecionados via argumento.

    Tem o objetivo de mostrar todas as Turmas e seus itens selecionados via argumento,
    em ordem alfabética, bem como a Carga Horária disponível, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Turmas cadastradas:')
    for cohort in sorted(cohorts, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {cohort[key]}' for key in keys_to_display if key in cohort]) + f' - Carga Horária disponível: {375 - (sum(disc["Carga Horária"] for disc in cohort["Disciplinas"]))}')

def print_cohorts_with_vacancies(keys_to_display):
    """print_cohorts_with_vacancies: Exibe todas as Turmas e os itens selecionados via argumento.

    Tem o objetivo de mostrar todas as Turmas e seus itens selecionados via argumento,
    em ordem alfabética, bem como a quantidade de vagas disponíveis, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Turmas com vagas:')
    for cohort in sorted(cohorts, key=lambda x: x['Nome']):
        if (40 - (sum(cohort["Alunos"]))) > 0:
            print (' - '.join([f'{key}: {cohort[key]}' for key in keys_to_display if key in cohort]) + f' - Vagas Disponíveis: {40 - (sum(cohort["Alunos"]))}')

def students_on_cohort():
    """students_on_cohort: Matricula Alunos em uma Turma.

    Compara, Calcula e Executa funções responsáveis por exibir, receber, calcular,
    comparar e alocar Alunos ainda não matriculados em uma Turma com vaga disponível
    """
    answer = 0
    while answer != 'menu':
        keys_to_display = ('Nome', 'Código')
        print_cohorts_with_vacancies(keys_to_display)
        index, vacancies = get_cohort_with_vacancies() #Recebe Turma selecionada
        print(f'\nTurma {cohorts[index]["Nome"]} selecionada.')
        keys_to_display = ('Nome', 'Matrícula')
        while vacancies > 0 and any('Turma' not in student for student in students):
            print_students_wo_cohort(keys_to_display)
            answer = input('Insira o Código do Aluno para matriculá-lo ou "menu" para voltar ao MENU PRINCIPAL: ')
            if answer == 'menu':
                break
            for student in students:
                if answer in student.values():
                    student['Turma'] = [{'Nome': cohorts[index]['Nome'], 'Código': cohorts[index]['Código']}]
                    cohorts[index]['Alunos'].append({'Nome': student['Nome'], 'Matrícula': student['Matrícula']})
                    vacancies -= 1
                    print('\nAluno matriculado com sucesso!')
                    if not any('Turma' not in student for student in students): #Sem alunos disponíveis volta pro MENU
                        print('\nAcabaram os alunos disponíveis para matrícula.')
                        answer = 'menu'
                    elif vacancies == 0 and any(len(cohort['Alunos'] < 40 for cohort in cohorts)): #Turma esgotada, mas há Turma(s) disponível(is)
                        answer = input('\nEssa Turma chegou ao limite de vagas.' #Volta pro MENU ou seleciona outra Turma
                                        '\nInsira "menu" para voltar ao MENU PRINCIPAL ou outra coisa para selecionar outra Turma: ')

def get_cohort_with_vacancies():
    """get_cohort_with_vacancies: Recebe uma Turma com vagas.

    Solicita e Recebe o Código da Turma escolhida e Executa funções
    que, juntas, verificam que o usuário irá inserir uma Turma que 
    tenha vagas disponíveis para matrícula de alunos.

    Returns:
        index int: Índice da Turma apta selecionada.
        vacancies int: Número de vagas na Turma apta selecionada.
    """
    while True:
        try:
            cohort_code = input('\nInsira o Código da Turma que deseja matricular Alunos: ')
            index = code_verifier_index(cohort_code, cohorts)
            vacancies = check_available_vacancies(index)
            return index, vacancies
        except ValueError as e:
            print(f'{e}')

def check_available_vacancies(index):
    """check_available_vacancies: Verifica se há, e entrega o valor de vagas disponíveis em uma Turma.

    Verifica se há, e entrega o valor de vagas disponíveis em uma Turma.

    Args:
        index int: Índice da Turma a ser verificada.

    Raises:
        ValueError: Informa que não há vagas nessa turma e garante que
                    a função geradora solicite novo Código de Turma antes
                    dela retornar valores para a sua função geradora.

    Returns:
        vacancies int: Número de vagas na Turma sendo verificada.
    """
    vacancies = (40 - (sum(cohorts[index]["Alunos"])))
    if vacancies > 0:
        return vacancies
    raise ValueError('\nErro! Essa Turma não tem vagas disponíveis.')

def print_students_of_cohort_using_code(cohort_code, cohorts_list):
    """print_students_of_cohort_using_code: Exibe os Alunos de uma Turma usando o Código dela.

    Exibe os Alunos de uma Turma usando o Código dela como argumento.

    Args:
        cohort_code str: Código único da Turma consultada.
        cohorts_list list[dict]: Lista de Dicionários de Turmas.
    """
    students = next((cohort['Alunos'] for cohort in cohorts_list if cohort['Código'] == cohort_code), None)
    for student in sorted(students, key=lambda x: x['Nome']):
        print (f'{student["Nome"]}')

def print_discs_of_cohort_using_code(cohort_code, cohorts_list):
    """print_discs_of_cohort_using_code: Exibe as Disciplinas de uma Turma usando o Código dela.

    Exibe as Disciplinas de uma Turma usando o Código dela como argumento.

    Args:
        cohort_code str: Código único da Turma consultada.
        cohorts_list list[dict]: Lista de Dicionários de Turmas.
    """
    discs = next((cohort['Disciplinas'] for cohort in cohorts_list if cohort['Código'] == cohort_code), None)
    for disc in sorted(discs, key=lambda x: x['Nome']):
        print (f'{disc["Nome"]}')