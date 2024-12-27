from random import choice
from faker import Faker
fake = Faker('pt_BR')

teachers = []

def registering_teachers():
    name = input('\nInsira o nome: ')
    id = create_teacher_id()
    birthday = str.input('\n Insira a Data de Nascimento: ')
    gender = input('\nInsira o Sexo (M, F ou NB): ')
    adress = input('\nInsira o Endereço: ')
    telephone = input('\nInsira o Telefone: ')
    email = input('\nInsira o E-mail:')
    teachers.append = create_teacher_dict(name, id, birthday, gender, adress, telephone, email)
    
    
def create_teacher_dict(name, id, birthday, gender, adress, telephone, email):
    return {'Nome': name, 'Matrícula': id, 'Data de Nascimento': birthday, 'Sexo': gender, 'Endereço': adress, 'Telefone': telephone, 'E-mail': email}

def create_teacher_id():
    id = f"{fake.random_number(digits=6, fix_len=True)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    return id