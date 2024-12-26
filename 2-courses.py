from random import choice
from faker import Faker
fake = Faker('pt_BR')

def create_course(course_name):
    """With the course name, create its code 

    Args:
        course_name (str): The course name

    Returns:
        dict: a dict that associates name of the course and its code 
    """
    name = course_name
    course_code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=4, fix_len=True)}"
    
    return {'Nome': name, 'Código do Curso': course_code}