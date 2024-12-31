from random import choice
from faker import Faker
fake = Faker('pt_BR')

disciplines = []

def registering_disciplines():
    name, index = rec_disc_name()
    disc_code = create_disc_code()
    workload = rec_disc_workload(name)
    if index is None:
        disciplines.append(create_disc_dict(name, disc_code, workload))
    else:
        disciplines[index] = create_disc_dict(name, disc_code, workload)

def rec_disc_name():
    name = input('\nInsira o Nome da Disciplina: ').upper()
    repeated_name, index = already_exists_tester(name)
    if repeated_name:
        if ask_solution(name) == 'c':
            return rec_disc_name()
        return name, index
    return name, None

def already_exists_tester(name):
    for i, dictionary in enumerate(disciplines):
        if name in dictionary.values():
            return True, i
    return False, None

def ask_solution(name):
    while True:
        user_solution = input(
            f'\nJá existe uma Disciplina cadastrada com o Nome: "{name}"
            \nInsira "C" para corrigir o Nome da Disciplina a ser cadastrada, ou "S" para Sobrescrevê-la: ').lower()
        if user_solution in ('c', 's'):
            return user_solution
        else:
            print('\nErro! Resposta Inválida. Tente novamente.')

def rec_disc_workload(name):
    available = False
    workloads_available = [15, 30, 45, 60, 75, 90, 105, 120]
    while not available:
        try:
            workload = int(input(f'\nInsira a Carga Horária de {name}: '))
            if workload in workloads_available:
                available = True
                return workload
            else:
                raise ValueError
        except ValueError:
            print('\nErro: As Cargas Horárias disponíveis são: 15, 30, 45, 60, 75, 90, 105 e 120. Tente novamente.')

def create_disc_code():
    code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=5, fix_len=True)}"
    return code

def create_disc_dict(name, code, workload):
    return {'Nome': name, 'Código': code, 'Carga Horária': workload}