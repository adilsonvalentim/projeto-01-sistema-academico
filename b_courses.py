from random import choice
from faker import Faker
fake = Faker('pt_BR')
from g_util import OperationCancelled

courses = []

def registering_courses():
    """registering_courses: Função principal da criação de Cursos.

    Chama as Funções necessárias para a obtenção dos dados, bem como suas verificações.
    Também chama a criação e alicação do dicionário na lista de cursos.
    """
    name = rec_course_name()
    code = create_course_code()
    courses.append(create_course_dict(name, code))
    print_sucess()
    
def rec_course_name():
    """rec_course_name: Solicita o Nome do Curso.

    Solicita o Nome do Curso.

    Returns:
        name str: Nome do Curso (único)
    """
    while True:
        name = input('\nInsira o Nome do Curso que deseja cadastrar: ').upper()
        repeated_name = already_exists_tester(name)
        if repeated_name:
            print(f'\nJá existe um Curso cadastrado com o nome {name}.'
                    '\nTente outro nome para realizar o cadastro.')
        else:
            return name

def already_exists_tester(name):
    """already_exists_tester: Testa se Nome é repetido.

    Testa se o Nome é repetido.

    Args:
        name str: Nome do Curso inserido pelo usuário.

    Returns:
        True ou False - bool: True se Nome repetido, senão False.
    """
    for dictionary in courses:
        if name in dictionary.values():
            return True
        else:
            return False

def create_course_code():
    """create_disc_code: Criador do Código único de Cursos

    Tem como função apenas criar um código único e retorná-lo quando é chamada.

    Returns:
        code str: Código no formato X####, onde X representa Letra Maiúscula e # representa número inteiro entre 0 e 9
    """
    course_code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=4, fix_len=True)}"
    return course_code

def create_course_dict(name, code):
    """create_disc_dict: Criador do Dicionário do Curso

    Sua função é processar os dados inseridos na Função Principal e retorná-los em formato de
    dicionário.

    Args:
        name str: Nome do Curso
        code str: Código do Curso

    Returns:
        dicionário do curso dict: Dicionário original do Curso, contendo Nome e Código.
    """
    return {'Nome': name, 'Código': code}

def print_sucess():
    """print_sucess: Exibe que o Curso foi cadastrado com sucesso.

    Informa ao usuário que o Curso foi cadastrado com êxito, e também exibe o Código do Curso.
    """
    print(f'\nCurso cadastrado com sucesso:\n{' - '.join([f'{key}: {value}' for key, value in courses[-1].items()])}')

def print_courses():
    """print_courses: Exibe todos os Cursos e seus Códigos.

    Tem o objetivo de mostrar todos os Cursos e seus Códigos em ordem alfabética, quando for chamada.
    """
    for course in sorted(courses, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {course[key]}' for key in course]))
