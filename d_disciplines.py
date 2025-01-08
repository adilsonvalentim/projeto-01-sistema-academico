from random import choice
from faker import Faker
fake = Faker('pt_BR')
from c_cohorts import print_cohorts_with_workload, print_cohorts, print_discs_of_cohort_using_code, cohorts
from e_teachers import teachers, print_teachers_with_workload, print_teachers, print_discs_of_teacher_using_id
from g_util import id_verifier_index, cohort_have_disc, cohort_name_using_code, exists_cohort_with_this_code, teacher_name_using_id, teacher_have_disc, exists_teacher_with_this_id, teacher_available_workload, cohort_available_workload, code_verifier_index

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
            f'\nJá existe uma Disciplina cadastrada com o Nome: "{name}"'
            '\nInsira "C" para corrigir o Nome da Disciplina a ser cadastrada, ou "S" para Sobrescrevê-la: ').lower()
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

def print_disciplines_available_to_teacher(keys_to_display):
    """print_disciplines_available_to_teacher: Exibe todas as Disciplinas disponíveis para Professores.

    Tem o objetivo de mostrar todas as Disciplinas disponíveis para Professores e seus itens selecionados
    via argumento, em ordem alfabética, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Disciplinas cadastradas disponíveis:')
    for discipline in sorted(disciplines, key=lambda x: x['Nome']):
        if 'Professor' not in discipline:
            print (' - '.join([f'{key}: {discipline[key]}' for key in keys_to_display if key in discipline]))

def print_disciplines_available_to_cohort(keys_to_display):
    """print_disciplines_available_to_cohort: Exibe todas as Disciplinas disponíveis para Turmas.

    Tem o objetivo de mostrar todas as Disciplinas disponíveis para Turmas e seus itens selecionados
    via argumento, em ordem alfabética, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Disciplinas cadastradas disponíveis:')
    for discipline in sorted(disciplines, key=lambda x: x['Nome']):
        if 'Turma' not in discipline:
            print (' - '.join([f'{key}: {discipline[key]}' for key in keys_to_display if key in discipline]))

'''def print_disciplines(keys_to_display):
    """print_disciplines: Exibe todas as Disciplinas e os itens selecionados via argumento.

    Tem o objetivo de mostrar todas as Disciplinas e seus itens selecionados
    via argumento, em ordem alfabética, quando for chamada.

    Args:
        keys_to_display tuple: Tupla com as chaves, cujos items devem ser impressos.
    """
    print('\nEstas são as Disciplinas cadastradas:')
    for discipline in sorted(disciplines, key=lambda x: x['Nome']):
        print (' - '.join([f'{key}: {discipline[key]}' for key in keys_to_display if key in discipline]))'''

def disciplines_on_teacher():
    """disciplines_on_teacher: Alocar Disciplinas a Professor.

    Compara, Calcula e Executa funções responsáveis por exibir, receber,
    calcular, comparar e alocar Disciplinas ainda sem Professor em um
    Professor com Carga Horária disponível, registrando em ambos a sua associação.

    Raises:
        ValueError: Garantem o Fluxo, informando problemas nas inserções
                    do usuário e retornando em locais adequados para que
                    usuário possa realizar nova inserção.
    """
    keys_to_display = ('Nome', 'Matrícula')
    print('\nEstes são os Professores cadastrados:')
    print_teachers_with_workload(keys_to_display)
    while True:
        try:
            id_selected = input('\nInsira a Matrícula do Professor que deseja alocar Disciplinas: ')
            t_index = id_verifier_index(id_selected, teachers)
            print(f'\nProfessor(a) {teachers[t_index]['Nome']} selecionado(a).')
            break
        except ValueError:
            print('\nErro! Matrícula inválida. Verifique e tente novamente.')
    keys_to_display = ('Nome', 'Código', 'Carga Horária')
    print_disciplines_available_to_teacher(keys_to_display)
    while True:
        try:
            available_workload = teacher_available_workload(teachers, t_index)
            disc_selected = input(f'\nO Professor(a) {teachers[t_index]['Nome']} possui {available_workload} horas disponíveis.\n'
                                'Insira o Código da Disciplina a ser alocada, ou "menu" para voltar ao MENU PRINCIPAL: ')
            if disc_selected == 'menu':
                return
            d_index = code_verifier_index(disc_selected, disciplines)
            if disciplines[d_index]['Carga Horária'] > available_workload:
                while True:
                    decision = input('\nProfessor não possui Carga Horária disponível para essa Disciplina\n'
                                'Insira "s" para selecionar outra Disciplina ou "menu" para voltar ao MENU PRINCIPAL: ').lower()
                    if decision == 's':
                        raise ValueError(f'{print_disciplines_available_to_teacher(keys_to_display)}')
                    if decision == 'menu':
                        return
                    else:
                        print('\nInserção inválida! Insira "s" ou "menu".')
            else:
                teachers[t_index]['Disciplinas'].append(disciplines[d_index])
                disciplines[d_index].setdefault('Professor', []).append({'Nome': teachers[t_index]['Nome'], 'Matrícula': teachers[t_index]['Matrícula']})
                print('\nDisciplina alocada com sucesso ao Professor.')
                if any('Professor' not in discipline for discipline in disciplines):
                    while True:
                        keep_adding = input('\nInsira "s" para alocar outra Disciplina, ou "menu" para voltar ao MENU PRINCIPAL: ').lower()
                        if keep_adding == 's':
                            raise ValueError(f'{print_disciplines_available_to_teacher(keys_to_display)}')
                        if keep_adding == 'menu':
                            return
                        else:
                            print('\nInserção inválida! Insira "s" ou "menu"')
                else:
                    print('\nNão existem mais Disciplinas disponíveis para serem alocadas. Voltando ao MENU PRINCIPAL.')
                    return
        except ValueError as e:
            print(f'{e}')

def disciplines_on_cohort():
    """disciplines_on_cohort: Alocar Disciplinas a Turma.

    Compara, Calcula e Executa funções responsáveis por exibir, receber,
    calcular, comparar e alocar Disciplinas ainda sem Turma em uma
    Turma com Carga Horária disponível, registrando em ambos a sua associação.

    Raises:
        ValueError: Garantem o Fluxo, informando problemas nas inserções
                    do usuário e retornando em locais adequados para que
                    usuário possa realizar nova inserção.
    """
    keys_to_display = ('Nome', 'Código')
    print('\nEstas são as Turmas cadastradas:')
    print_cohorts_with_workload(keys_to_display)
    while True:
        try:
            code_selected = input('\nInsira o Código da Turma que deseja alocar Disciplinas: ')
            c_index = code_verifier_index(code_selected, cohorts)
            print(f'\nTurma {cohorts[c_index]['Nome']} selecionada.')
            break
        except ValueError as e:
            print(f'\n{e}')
    keys_to_display = ('Nome', 'Código', 'Carga Horária')
    print_disciplines_available_to_cohort(keys_to_display)
    while True:
        try:
            available_workload = cohort_available_workload(cohorts, c_index)
            disc_selected = input(f'\nA Turma {cohorts[c_index]['Nome']} possui {available_workload} horas disponíveis.\n'
                                'Insira o Código da Disciplina a ser alocada, ou "menu" para voltar ao MENU PRINCIPAL: ')
            if disc_selected == 'menu':
                return
            d_index = code_verifier_index(disc_selected, disciplines)
            if disciplines[d_index]['Carga Horária'] > available_workload:
                while True:
                    decision = input('\nTurma não possui Carga Horária disponível para essa Disciplina\n'
                                'Insira "s" para selecionar outra Disciplina ou "menu" para voltar ao MENU PRINCIPAL: ').lower()
                    if decision == 's':
                        raise ValueError(f'{print_disciplines_available_to_cohort(keys_to_display)}')
                    if decision == 'menu':
                        return
                    else:
                        print('\nInserção inválida! Insira "s" ou "menu".')
            else:
                cohorts[c_index]['Disciplinas'].append(disciplines[d_index])
                disciplines[d_index].setdefault('Turma', []).append({'Nome': cohorts[c_index]['Nome'], 'Matrícula': cohorts[c_index]['Matrícula']})
                print('\nDisciplina alocada com sucesso na Turma.')
                if any('Turma' not in discipline for discipline in disciplines):
                    while True:
                        keep_adding = input('\nInsira "s" para alocar outra Disciplina, ou "menu" para voltar ao MENU PRINCIPAL: ').lower()
                        if keep_adding == 's':
                            raise ValueError(f'{print_disciplines_available_to_cohort(keys_to_display)}')
                        if keep_adding == 'menu':
                            return
                        else:
                            print('\nInserção inválida! Insira "s" ou "menu"')
                else:
                    print('\nNão existem mais Disciplinas disponíveis para serem alocadas. Voltando ao MENU PRINCIPAL.')
                    return
        except ValueError as e:
            print(f'{e}')

def consult_discs_of_teacher():
    """consult_discs_of_teacher: Exibe as Disciplinas do Professor selecionado.

    Recebe, Calcula, Exibe e Executa funções responsáveis por receber,
    calcular e exibir as Disciplinas alocadas no Professor selecionado.
    """
    keys_to_display = ('Nome', 'Matrícula')
    print_teachers(keys_to_display)
    completed = False
    while not completed:
        user_teacher_id = input('\nInsira a Matrícula do Professor para consultar as suas Disciplinas: ')
        if exists_teacher_with_this_id(user_teacher_id, teachers):
            if teacher_have_disc(user_teacher_id, teachers):
                print(f'\n{teacher_name_using_id(user_teacher_id, teachers)} é o Professor das seguintes Disciplinas:')
                print_discs_of_teacher_using_id(user_teacher_id, teachers)
            else:
                print(f'\nO Professor {teacher_name_using_id(user_teacher_id, teachers)} não possui Disciplinas alocadas.')
            completed = True
        else:
            print('\nNão existe Professor com a Matrícula Inserida. Verifique e tente novamente.')

def consult_discs_of_cohort():
    """consult_discs_of_cohort: Exibe as Disciplinas da Turma selecionada.

    Recebe, Calcula, Exibe e Executa funções responsáveis por receber,
    calcular e exibir as Disciplinas alocadas na Turma selecionada.
    """
    keys_to_display = ('Nome', 'Código')
    print_cohorts(keys_to_display)
    completed = False
    while not completed:
        user_cohort_code = input('\nInsira o Código da Turma para consultar as suas Disciplinas: ')
        if exists_cohort_with_this_code(user_cohort_code, cohorts):
            if cohort_have_disc(user_cohort_code, cohorts):
                print(f'\nA Turma {cohort_name_using_code(user_cohort_code, cohorts)} possui as seguintes Disciplinas:')
                print_discs_of_cohort_using_code(user_cohort_code, cohorts)
            else:
                print(f'\nA Turma {cohort_name_using_code(user_cohort_code, cohorts)} não possui Disciplinas alocadas.')
            completed = True
        else:
            print('\nNão existe Turma com o Código inserido. Verifique e tente novamente.')