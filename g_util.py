from re import match
from datetime import datetime

def code_existance_verifier(user_code, codes_list):
    for dictionary in codes_list:
        if user_code in dictionary.values():
            return True, dictionary['Nome']
    return False, None

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