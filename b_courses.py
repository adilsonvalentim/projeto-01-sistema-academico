from random import choice
from faker import Faker
fake = Faker('pt_BR')

courses = []

def registering_courses():
    name = input('\nInsira o Nome do Curso: ')
    code = create_course_code()
    courses.append() = create_course_dict(name, code)

def create_course_dict(name, code):
    return {'Nome': name, 'Código': code}

def create_course_code():
    course_code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=4, fix_len=True)}"
    return course_code

def print_courses():
    for course in courses:
        print (' - '.join([f'{key}: {value}' for key, value in course.items()]))