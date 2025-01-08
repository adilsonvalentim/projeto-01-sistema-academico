from re import match
from datetime import datetime

def exists_disc_with_this_code(disc_code, discs_list):
    """exists_disc_with_this_code: Verifica se existe Disciplina com o Código do argumento.

    Verifica se existe Disciplina com o Código do argumento.

    Args:
        disc_code str: Código da Disciplina inserido pelo usuário.
        discs_list list[dict]: Lista de dicionários de Disciplinas.

    Returns:
        True ou False bool: True se existe Disciplina com esse Código, senão False.
    """
    if any(discipline['Código'] == disc_code for discipline in discs_list):
        return True
    else:
        return False

def exists_cohort_with_this_code(cohort_code, cohorts_list):
    """exists_cohort_with_this_code: Verifica se existe Turma com o Código do argumento.

    Verifica se existe Turma com o Código do argumento.

    Args:
        cohort_code str: Código da Turma inserido pelo usuário.
        cohorts_list list[dict]: Lista de dicionários de Turmas.

    Returns:
        True ou False bool: True se existe Turma com esse Código, senão False.
    """
    if any(cohort['Código'] == cohort_code for cohort in cohorts_list):
        return True
    else:
        return False

def exists_teacher_with_this_id(teacher_id, teachers_list):
    """exists_teacher_with_this_id: Verifica se existe Professor com a Matrícula do argumento.

    Verifica se existe Professor com a Matrícula do argumento.

    Args:
        teacher_id str: Matrícula do Professor inserida pelo usuário.
        teachers_list list[dict]: Lista de dicionários de Professores.

    Returns:
        True ou False bool: True se existe Professor com esse Matrícula, senão False.
    """
    if any(teacher['Matrícula'] == teacher_id for teacher in teachers_list):
        return True
    else:
        return False

def disc_have_teacher(disc_code, disc_list):
    """disc_have_teacher: Verifica se a Disciplina tem Professor responsável.

    Verifica se a Disciplina tem Professor responsável, usando o código como argumento.

    Args:
        disc_code str: Código da Disciplina sendo verificada.
        disc_list list[dict]: Lista de dicionários de Disciplinas.

    Returns:
        True ou False bool: True se a Disciplina tem Professor responsável, senão False.
    """
    for disc in disc_list:
        if disc['Código'] == disc_code:
            if 'Professor' in disc:
                return True
            else:
                return False
            
def cohort_have_disc(cohort_code, cohorts_list):
    """cohort_have_disc: Verifica se a Turma tem alguma Disciplina alocada.

    Verifica se a Turma tem alguma Disciplina alocada, usando o código como argumento.

    Args:
        cohort_code str: Código da Turma sendo verificada.
        cohorts_list list[dict]: Lista de dicionários de Turmas.

    Returns:
        True ou False bool: True se a Turma tem alguma Disciplina alocada, senão False.
    """
    for cohort in cohorts_list:
        if cohort['Código'] == cohort_code:
            if cohort['Disciplinas']:
                return True
            else:
                return False

def cohort_have_students(cohort_code, cohorts_list):
    """cohort_have_students: Verifica se a Turma tem algum Aluno matriculado.

    Verifica se a Turma tem algum Aluno matriculado, usando o código como argumento.

    Args:
        cohort_code str: Código da Turma sendo verificada
        cohorts_list list[dict]: Lista de dicionários de Turmas.

    Returns:
        True ou False bool: True se a Turma tem algum Aluno matriculado, senão False.
    """
    for cohort in cohorts_list:
        if cohort['Código'] == cohort_code:
            if cohort['Alunos']:
                return True
            else:
                return False

def teacher_have_disc(teacher_id, teachers_list):
    """teacher_have_disc: Verifica se o Professor tem alguma Disciplina alocada.

    Verifica se o Professor tem alguma Disciplina alocada, usando o código como argumento.

    Args:
        teacher_id str: Código do Professor sendo verificado.
        teachers_list list[dict]: Lista de dicionários de Professores.

    Returns:
        True ou False bool: True se o Professor tem alguma Disciplina alocada, senão False.
    """
    for teacher in teachers_list:
        if teacher['Matrícula'] == teacher_id:
            if teacher['Disciplinas']:
                return True
            else:
                return False

def teacher_of_disc_using_disc_code(disc_code, disc_list):
    """teacher_of_disc_using_disc_code: Consulta o Professor de determinada Disciplina.

    Consulta o Professor de determinada Disciplina, usando o código da Disciplina como argumento.

    Args:
        disc_code str: Código da Disciplina inserida.
        disc_list list[dict]: Lista de dicionários de Disciplinas.

    Returns:
        Nome do Professor str: Nome do Professor da Disciplina consultada.
    """
    for disc in disc_list:
        if disc['Código'] == disc_code:
            if isinstance(disc.get('Professor'), list) and disc['Professor']:
                return disc['Professor'][0]['Nome']
            elif isinstance(disc.get('Professor'), dict):
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