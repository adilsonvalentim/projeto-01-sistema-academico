from random import choice
from faker import Faker
from g_util import OperationCancelled, calc_age, check_phone, check_email
fake = Faker('pt_BR')

teachers = []

def registering_teachers():
    """registering_teachers: Função principal para o cadastro de Professores

    Chama funções para recolhimento de dados do professor, criação de Matrícula
    e criação do dicionário original do professor.
    """
    name = rec_name()
    birthday = rec_birthday()
    gender = rec_gender()
    adress = rec_adress()
    phone = rec_phone()
    email = rec_email()
    id = create_teacher_id()
    teachers.append = create_teacher_dict(name, id, birthday, gender, adress, phone, email)

def rec_name():
    """rec_name: Receber o Nome do Professor.

    Recebe, deixa em caixa alta e retorna o Nome.

    Returns:
        name str: Nome.
    """
    name = input('\nInsira o Nome do professor: ').upper()
    return name

def rec_birthday():
    """rec_birthday: Receber a Data de Nascimento do Professor.

    Recebe, chama verificação de formato e de validade,
    verifica idade e retorna a Data de Nascimento.

    Raises:
        ValueError: Caso a idade não seja compatível, solicita que usuário
        verifique a Data de Nascimento.

    Returns:
        birthday str: Data de Nascimento no formato DD/MM/AAAA.
    """
    while True:
        try:
            birthday = input('\nUsando o formato DD/MM/AAAA, insira a Data de Nascimento do professor: ')
            age = calc_age(birthday)
            if not 20 <= age <= 80:
                raise ValueError('|||||||||O professor não pode ter menos de 20, nem mais de 80 anos. Verifique a Data de Nascimento.')
        except ValueError as e:
            print(f'\nErro! {e}')
        return birthday

def rec_gender():
    """rec_gender: Receber o Sexo do Professor.

    Recebe, verifica se o valor é válido e retorna o Sexo.

    Returns:
        gender str: Sexo ('M', 'F' ou 'NB').
    """
    while True:
        gender = input('\nInsira o Sexo do professor (M, F ou NB): ').strip("'").strip('"').upper()
        if gender in ('M', 'F', 'NB'):
            return gender
        print('\nErro! Inserção Inválida. Insira "M", "F" ou "NB"')

def rec_adress():
    """rec_adress: Receber o Endereço do Professor.

    Recebe, deixa em caixa alta e retorna o Endereço.

    Returns:
        adress str: Endereço.
    """
    adress = input('\nInsira o Endereço do professor: ').upper()
    return adress

def rec_phone():
    """rec_phone: Receber o Telefone do Professor.

    Recebe, chama verificação de formato e retorna o Telefone.

    Returns:
        check_phone def: Uma função verificadora que retorna uma str com o Telefone.
    """
    while True:
        try:
            phone = input('\nInsira o Telefone do professor (Formato "(##)#####-####"): ').strip('"').strip("'")
            return check_phone(phone)
        except ValueError:
            print('\nErro! Formato de Telefone inválido.')

def rec_email():
    """rec_email: Receber o E-mail do Professor.

    Recebe, chama verificação de formato e retorna o E-mail.

    Returns:
        check_email def: Uma função verificadora que retorna uma str com o E-mail.
    """
    while True:
        try:
            email = input('\nInsira o e-mail do professor (ex: nome@domínio.ext): ')
            return check_email(email)
        except ValueError:
            print('\nErro! Formato de email inválido.')

def create_teacher_id():
    """create_teacher_id: Criar o Código Único do Professor.

    Ao ser chamada, gera e retorna um Código Único.

    Returns:
        id str: Código do professor, no formato ######X, onde # é um algarismo e X é uma letra maiúscula.
    """
    id = f"{fake.random_number(digits=6, fix_len=True)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    return id

def create_teacher_dict(name, id, birthday, gender, adress, phone, email):
    """create_teacher_dict: Criar o Dicionário do Professor.

    Recebe os dados necessários e retorna o dicionário original do Professor.

    Args:
        name str: Nome.
        id str: Código.
        birthday str: Data de Nascimento.
        gender str: Sexo.
        adress str: Endereço.
        phone str: Telefone.
        email str: E-mail.

    Returns:
        dicionário do professor dict: Dicionário original do Professor, contendo Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone e E-mail.
    """
    return {'Nome': name, 'Matrícula': id, 'Disciplinas': [], 'Data de Nascimento': birthday, 'Sexo': gender, 'Endereço': adress, 'Telefone': phone, 'E-mail': email}

def print_teachers(keys_to_display):
    """print_teachers: Exibe todos os Professores, suas Matrículas e suas Horas-Aula.

    Tem o objetivo de mostrar todos os Professores, suas Matrículas e Suas Horas-Aula em ordem alfabética, quando for chamada.
    """
    for teacher in sorted(teachers, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {teacher[key]}' for key in keys_to_display if key in teacher]))