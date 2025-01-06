from random import choice
from faker import Faker
from g_util import OperationCancelled, calc_age, check_phone, check_email
fake = Faker('pt_BR')

students = []

def registering_students():
    """registering_students: Função principal para o cadastro de Alunos.

    Chama funções para recolhimento de dados do aluno, criação de Matrícula
    e criação do dicionário original do aluno.
    """
    name = rec_name()
    birthday = rec_birthday()
    gender = rec_gender()
    adress = rec_adress()
    phone = rec_phone()
    email = rec_email()
    id = create_student_id()
    students.append = create_student_dict(name, id, birthday, gender, adress, phone, email)

def rec_name():
    """rec_name: Receber o Nome do Aluno.

    Recebe, deixa em caixa alta e retorna o Nome.

    Returns:
        name str: Nome.
    """
    name = input('\nInsira o Nome do aluno: ').upper()
    return name

def rec_birthday():
    """rec_birthday: Receber a Data de Nascimento do Aluno.

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
            birthday = input('\nUsando o formato DD/MM/AAAA, insira a Data de Nascimento do aluno: ')
            age = calc_age(birthday)
            if not 18 <= age:
                raise ValueError('|||||||||O aluno não pode ter menos de 18 anos. Verifique a Data de Nascimento.')
        except ValueError as e:
            print(f'\nErro! {e}')
        return birthday

def rec_gender():
    """rec_gender: Receber o Sexo do Aluno.

    Recebe, verifica se o valor é válido e retorna o Sexo.

    Returns:
        gender str: Sexo ('M', 'F' ou 'NB').
    """
    while True:
        gender = input('\nInsira o Sexo do aluno (M, F ou NB): ').strip("'").strip('"').upper()
        if gender in ('M', 'F', 'NB'):
            return gender
        print('\nErro! Inserção Inválida. Insira "M", "F" ou "NB"')

def rec_adress():
    """rec_adress: Receber o Endereço do Aluno.

    Recebe, deixa em caixa alta e retorna o Endereço.

    Returns:
        adress str: Endereço.
    """
    adress = input('\nInsira o Endereço do aluno: ').upper()
    return adress

def rec_phone():
    """rec_phone: Receber o Telefone do Aluno.

    Recebe, chama verificação de formato e retorna o Telefone.

    Returns:
        check_phone def: Uma função verificadora que retorna uma str com o Telefone.
    """
    while True:
        try:
            phone = input('\nInsira o Telefone do aluno (Formato "(##)#####-####"): ').strip('"').strip("'")
            return check_phone(phone)
        except ValueError:
            print('\nErro! Formato de Telefone inválido.')

def rec_email():
    """rec_email: Receber o E-mail do Aluno.

    Recebe, chama verificação de formato e retorna o E-mail.

    Returns:
        check_email def: Uma função verificadora que retorna uma str com o E-mail.
    """
    while True:
        try:
            email = input('\nInsira o e-mail do aluno (ex: nome@domínio.ext): ')
            return check_email(email)
        except ValueError:
            print('\nErro! Formato de email inválido.')

def create_student_id():
    """create_student_id: Criar o Código Único do Aluno.

    Ao ser chamada, gera e retorna um Código Único.

    Returns:
        id str: Código do aluno, no formato ########X, onde # é um algarismo e X é uma letra maiúscula.
    """
    id = f"{fake.random_number(digits=8, fix_len=True)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    return id

def create_student_dict(name, id, birthday, gender, adress, phone, email):
    """create_student_dict: Criar o Dicionário do Aluno.

    Recebe os dados necessários e retorna o dicionário original do Aluno.

    Args:
        name str: Nome.
        id str: Código.
        birthday str: Data de Nascimento.
        gender str: Sexo.
        adress str: Endereço.
        phone str: Telefone.
        email str: E-mail.

    Returns:
        dicionário do aluno dict: Dicionário original do Aluno, contendo Nome, Matrícula, Data de Nascimento, Sexo, Endereço, Telefone e E-mail.
    """
    return {'Nome': name, 'Matrícula': id, 'Data de Nascimento': birthday, 'Sexo': gender, 'Endereço': adress, 'Telefone': phone, 'E-mail': email}