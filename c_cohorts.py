from b_courses import courses, print_courses
from g_util import code_existance_verifier, OperationCancelled

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
    """print_cohorts: Exibe todas as Turmas e os itens selecionados via argumento.

    Tem o objetivo de mostrar todos as Turmas e seus itens selecionados
    via argumento, em ordem alfabética, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Turmas cadastradas:')
    for cohort in sorted(cohorts, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {cohort[key]}' for key in keys_to_display if key in cohort]))