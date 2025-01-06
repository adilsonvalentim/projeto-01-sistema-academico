from re import match
from datetime import datetime

class OperationCancelled(Exception):
    pass

def code_existance_verifier(user_code, codes_list):
    for dictionary in codes_list:
        if user_code in dictionary.values():
            return True, dictionary['Nome']
    return False, None

def code_verifier_index(user_code, codes_list):
    for i, dictionary in enumerate(codes_list):
        if user_code in dictionary.values():
            return i
    raise ValueError('\nErro! Código inexistente. Verifique e tente novamente.')

def id_verifier_index(user_id, id_list):
    for i, dictionary in enumerate(id_list):
        if user_id in dictionary.values():
            return i
    raise ValueError

def teacher_available_workload(teachers, index):
    teacher_workload = 0
    for value in teachers[index]['Disciplinas']:
        teacher_workload += value.get('Carga Horária', 0)
    available_workload = 600 - teacher_workload
    return available_workload

def cohort_available_workload(cohorts, index):
    cohort_workload = 0
    for value in cohorts[index]['Disciplinas']:
        cohort_workload += value.get('Carga Horária', 0)
    available_workload = 375 - cohort_workload
    return available_workload

def calc_age(birthday):
    try:
        birth_date = datetime.strptime(birthday, '%d/%m/%Y')
    except ValueError:
        raise ValueError('Formato de data inválido. Utilize DD/MM/AAAA.')
    today = datetime.today()
    if birth_date > today:
        raise ValueError('A Data de Nascimento não pode estar no futuro.')
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def check_phone(phone):
    pattern = r'^\(\d{2}\)\d{5}-\d{4}$' #Padrão exigido 
    if match(pattern, phone): #Verificação se o telefone foi inserido respeitando o padrão exigido
        return phone
    raise ValueError

def check_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$' #Padrão exigido
    if match(pattern, email):
        return email
    raise ValueError