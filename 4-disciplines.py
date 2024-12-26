from random import choice
from faker import Faker
fake = Faker('pt_BR')

def create_discipline(discipline_name, discipline_workload):
    """With discipline name and workload, creates discipline code

    Args:
        discipline_name (str): The discipline name 
        discipline_workload (int): The discipline workload

    Returns:
        dict: a dict that associates name of the discipline and its code and worload
    """
    name = discipline_name
    discipline_code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=5, fix_len=True)}"
    workload = discipline_workload
    
    return {'Nome': name, 'Código da Disciplina': discipline_code, 'Carga Horária': workload}