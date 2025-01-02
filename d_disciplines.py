from random import choice
from faker import Faker
fake = Faker('pt_BR')

disciplines = []

def registering_disciplines():
    """registering_disciplines: A função principal da criação de novas disciplinas
    
    Funciona chamando outras defs necessárias para verificações e recebimentos de inputs, que possibilitarão
    a alocação de um dicionário preenchido com os dados de uma nova disciplina na lista de discilinas.
    """
    name, index = rec_disc_name()
    disc_code = create_disc_code()
    workload = rec_disc_workload(name)
    if index is None:
        disciplines.append(create_disc_dict(name, disc_code, workload))
    else:
        disciplines[index] = create_disc_dict(name, disc_code, workload)

def rec_disc_name():
    """rec_disc_name: Recebe o nome da Disciplina pelo usuário

    Recebe o nome da Disciplina. chama uma função de verificação de pré-existência.
    Se já existe, chama uma função que dá opções de solução para o usuário.

    Returns:
        name str: Nome da Disciplina inserida pelo usuário.
        index ou None - int ou NoneType: Índex da Disciplina a ser substituída, caso o usuário tenha decidido por sobrescrever a 
        pré-existente, ou None caso não se aplique.
        rec_disc_name() def: Reinicia a Função caso o usuário deseje corrigir o nome da Disciplina a ser cadastrada.
    """
    name = input('\nInsira o Nome da Disciplina que deseja cadastrar: ').upper()
    repeated_name, index = already_exists_tester(name)
    if repeated_name:
        if ask_solution(name) == 'c':
            return rec_disc_name()
        return name, index
    return name, None

def already_exists_tester(name):
    """already_exists_tester: Testa se já existe disciplina cadastrada com o nome que o usuário está tentando utilizar

    Verifica se o nome inserido pelo usuário para a disciplina que quer cadastrar já não existe, e caso exista irá retornar
    o índice na lista Disciplines, que já contém essa pré-existente.

    Args:
        name str: Nome da Disciplina inserida pelo usuário.

    Returns:
        True ou False - bool: Retorna True se nome for repetido, ou False se não for.
        i ou None - int ou NoneType: Índex da Disciplina repetida ou None, caso não se aplique.
    """
    for i, dictionary in enumerate(disciplines):
        if name in dictionary.values():
            return True, i
    return False, None

def ask_solution(name):
    """ask_solution: Pergunta e recebe do usuário o que fazer, uma vez que o nome da Disciplina é repetido.

    Informa o usuário que já existe uma disciplina com esse nome e oferece as opções de trocar o nome
    ou Sobrescrever as informações da disciplina pré-cadastrada em questão.

    Args:
        name str: Nome da Disciplina repetida.

    Returns:
        user_solution str: Um caractere que representa a solução escolhida pelo usuário.
    """
    while True:
        user_solution = input(
            f'\nJá existe uma Disciplina cadastrada com o Nome: "{name}"
            \nInsira "C" para corrigir o Nome da Disciplina a ser cadastrada, ou "S" para Sobrescrevê-la: ').lower()
        if user_solution in ('c', 's'):
            return user_solution
        else:
            print('\nErro! Resposta Inválida. Tente novamente.')

def rec_disc_workload(name):
    """rec_disc_workload: Recebe a Carga horária da Disciplina a ser cadastrada

    O usuário irá indicar a carga horária da Disciplina. A função irá recusar valores que não sejam os
    disponíveis e perguntará novamente até o usuário inserir um valor válido. Retornará o valor.

    Args:
        name str: Nome da Disciplina, cuja carga horária está sendo solicitada.

    Raises:
        ValueError: Verificação para garantir que o valor inserido para a carga horária seja válido

    Returns:
        workload int: Carga Horária inserida pelo usuário para a Disciplina em questão
    """
    available = False
    workloads_available = [15, 30, 45, 60, 75, 90, 105, 120]
    while not available:
        try:
            workload = int(input(f'\nAs Cargas Horárias disponíveis são: 15, 30, 45, 60, 75, 90, 105 e 120\nInsira a Carga Horária de {name}: '))
            if workload in workloads_available:
                available = True
                return workload
            else:
                raise ValueError
        except ValueError:
            print('\nErro: As Cargas Horárias disponíveis são: 15, 30, 45, 60, 75, 90, 105 e 120. Tente novamente.')

def create_disc_code():
    """create_disc_code: Criador do Código único de Disciplinas

    Tem como função apenas criar um código único e retorná-lo quando é chamada.

    Returns:
        code str: Código no formato X#####, onde X representa Letra Maiúscula e # representa número inteiro entre 0 e 9
    """
    code = f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=5, fix_len=True)}"
    return code

def create_disc_dict(name, code, workload):
    """create_disc_dict: Criador do Dicionário da Disciplina

    Sua função é processar os dados inseridos na Função Principal e retorná-los em formato de
    dicionário.

    Args:
        name str: Nome da Disciplina
        code str: Código da Disciplina
        workload int: Carga Horária da Disciplina

    Returns:
        dicionário da disciplina dict: Dicionário original da Disciplina, contendo Nome, Código e Carga Horária
    """
    return {'Nome': name, 'Código': code, 'Carga Horária': workload}