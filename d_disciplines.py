from random import choice
from faker import Faker
fake = Faker('pt_BR')

disciplines = []

def registering_disciplines():
    name = input('\nInsira o Nome da Disciplina: ')
    discipline_code = create_discipline_code()
    workload = input('\nInsira a Carga Horária da Disciplina: ')
    disciplines.append() = create_discipline_dict(name, discipline_code, workload)
    
def create_discipline_dict(name, code, workload):
    return {'Nome': name, 'Código': code, 'Carga Horária': workload}
    
def create_discipline_code():
    code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=5, fix_len=True)}"    