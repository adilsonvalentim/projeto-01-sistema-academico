from re import match
from datetime import datetime

class OperationCancelled(Exception):
    pass

def exists_disc_with_this_code(user_code, codes_list):
    if any(discipline['Código'] == user_code for discipline in codes_list):
        return True
    else:
        return False
    
def exists_cohort_with_this_code(user_code, codes_list):
    if any(cohort['Código'] == user_code for cohort in codes_list):
        return True
    else:
        return False
    
def exists_teacher_with_this_id(user_code, codes_list):
    if any(teacher['Matrícula'] == user_code for teacher in codes_list):
        return True
    else:
        return False

def disc_have_teacher(disc_code, disc_list):
    for disc in disc_list:
        if disc['Código'] == disc_code:
            if 'Professor' in disc:
                return True
            else:
                return False
            
def teacher_have_disc(teacher_id, teachers_list):
    for teacher in teachers_list:
        if teacher['Matrícula'] == teacher_id:
            if teacher['Disciplines']:
                return True
            else:
                return False

def cohort_have_disc(cohort_code, cohorts_list):
    for cohort in cohorts_list:
        if cohort['Código'] == cohort_code:
            if cohort['Disciplines']:
                return True
            else:
                return False
            
def cohort_have_students(cohort_code, cohorts_list):
    for cohort in cohorts_list:
        if cohort['Código'] == cohort_code:
            if cohort['Alunos']:
                return True
            else:
                return False
            
def teacher_of_disc_using_disc_code(disc_code, disc_list):
    for disc in disc_list:
        if disc['Código'] == disc_code:
                return disc['Professor']['Nome']

def disc_name_using_code(disc_code, disc_list):
    name = next((disc['Nome'] for disc in disc_list if disc['Código'] == disc_code), None)
    return name

def teacher_name_using_id(teacher_id, teachers_list):
    name = next((teacher['Nome'] for teacher in teachers_list if teacher['Matrícula'] == teacher_id), None)
    return name

def cohort_name_using_code(cohort_code, cohorts_list):
    name = next((cohort['Nome'] for cohort in cohorts_list if cohort['Código'] == cohort_code), None)
    return name
    
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