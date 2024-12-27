from b_courses import courses, print_courses
from g_util import code_existance_verifier

cohorts = []

def registering_cohorts():
    exists = False
    print('\nOs cursos cadastrados são:')
    print_courses()
    while not exists:
        user_code = input(f'Insira o Código do Curso do qual essa Turma fará parte: ').upper()
        exists = code_existance_verifier(user_code, courses)
        if not exists:
            print('\nCódigo inválido, tente novamente.')
    
    year = input('\nInsira o Ano dessa Turma, com dois dígitos (Ex: Se 2024, insira "24"): ')
    semester = input('\nInsira o Semestre dessa Turma (Ex: Se 1º Semestre, insira "1")')
            
    

def create_cohort_code(course_name, course_code, cohort_year, cohort_semester):
    name = f'{course_name} {cohort_year}{cohort_semester}'
    cohort_code = f'{course_code}{cohort_year}{cohort_semester}'
    
    return {'Nome': name, 'Código': cohort_code}