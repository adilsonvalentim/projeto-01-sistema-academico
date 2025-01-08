from b_courses import registering_courses, courses
from c_cohorts import registering_cohorts, students_on_cohort, cohorts
from d_disciplines import consult_discs_of_cohort, registering_disciplines, disciplines_on_teacher, consult_discs_of_teacher, disciplines_on_cohort, disciplines
from e_teachers import registering_teachers, consult_teacher_of_disc, teachers
from f_students import consult_students_of_cohort, registering_students, students

def title():
        """title: Título do Programa.

        Exibe o Título do Programa.
        """
        print('\n* * * * * SISTEMA ACADÊMICO * * * * *')

def ask_username():
        """ask_username: Recebe o nome do Usuário.

        Pergunta e recebe o nome do Usuário.

        Returns:
                username str: Nome do Usuário.
        """
        username = input('\nPor favor usuário, insira o seu nome: ')
        return username

def introduction(username):
        """introduction: Apresenta o programa.

        Apresenta o programa e suas funcionalidades.

        Args:
                username str: Nome do usuário.
        """
        print(f'\nOlá {username}, este programa é um Sistema Acadêmico. Nele, você poderá cadastrar Cursos, Turmas, Disciplinas,\n'
                'Professores e Alunos. Também poderá alocar Disciplinas aos Professores, Disciplinas às Turmas e matricular Alunos em Turmas.\n'
                'Por fim, poderá consultar Professores por Disciplinas, Disciplinas por Professores, Alunos por Turmas, Disciplinas por Turmas.\n'
                'Para realizar Cadastros, Alocações, Matrículas e Consultas, você deverá inserir o número correspondente no MENU PRINCIPAL.')

def main_menu():
        """main_menu: Menu Principal.

        Exibe todas as opções de funcionalidades e seus índices.
        """
        print('\n* * * MENU PRINCIPAL * * *\n'
                '1 - Cadastrar Curso\n'#ok
                '2 - Cadastrar Turma\n'#ok
                '3 - Cadastrar Disciplina\n'#ok
                '4 - Cadastrar Professor\n'#ok
                '5 - Cadastrar Aluno\n'#ok
                '6 - Alocar Disciplinas a Professor\n'#Construido em Disciplinas
                '7 - Alocar Disciplinas a Turma\n' #Construido em Disciplinas
                '8 - Matricular Aluno em Turma\n' #Construído em Turmas 
                '9 - Consultar Professor por Disciplina\n' #Construído em Professores
                '10 - Consultar Disciplinas por Professor\n' #Construído em Disciplinas
                '11 - Consultar Alunos por Turma\n' #Construído em Alunos
                '12 - Consultar Disciplinas por Turma\n' #Construído em Disciplinas
                'sair - Encerra o Programa')

def choose_option():
        """choose_option: Recebe o índice da opção do usuário.

        Pergunta e recebe o índice da opção escolhida do usuário.

        Returns:
                option str: Índice da Opção.
        """
        option = 0
        option = input('\nPor favor, insira o índice da função que deseja executar: ').lower()
        return option

def option_executor():
        """option_executor: Executor da opção escolhida.

        Executa a opção escolhida pelo usuário.

        Returns:
                True ou False bool: True volta ao MENU PRINCIPAL após executar a função escolhida,
                                        False leva ao fim do programa.
        """
        keep_working_options = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        while True:
                option = choose_option()
                if option == 'sair':
                        return False
                elif option in keep_working_options:
                        if option == '1': #Cadastra Curso
                                registering_courses()
                        if option == '2': #Cadastra Turma
                                if courses:
                                        registering_cohorts()
                                else:
                                        print('\nErro! Cadastre algum Curso antes de cadastrar alguma Turma.')
                        if option == '3': #Cadastra Disciplina
                                registering_disciplines()
                        if option == '4': #Cadastra Professor
                                registering_teachers()
                        if option == '5': #Cadastra Aluno
                                registering_students()
                        if option == '6': # Aloca Disciplinas a Professor
                                if not teachers:
                                        print('\nErro! Não há Professores cadastrados.')
                                elif not disciplines:
                                        print('\nErro! Não há Disciplinas cadastradas.')
                                elif any('Professor' not in discipline for discipline in disciplines):
                                                disciplines_on_teacher()
                                else:
                                        print('\nErro! Todas as Disciplinas já possuem Professor alocado.'
                                                '\nCadastre uma nova Disciplina, e tente novamente.')
                        if option == '7': # Aloca Disciplinas a Turma
                                if not cohorts:
                                        print('\nErro! Não há Turmas cadastradas.')
                                elif not disciplines:
                                        print('\nErro! Não há Disciplinas cadastradas.')
                                elif any('Turma' not in discipline for discipline in disciplines):
                                        disciplines_on_cohort()
                                else:
                                        print('\nErro! Todas as Disciplinas já estão alocadas em Turmas.'
                                                '\nCadastre uma nova Disciplina, e tente novamente.')
                        if option == '8': #Matricula Aluno em Turma
                                if not cohorts:
                                        print('\nErro! Não há Turmas cadastradas.')
                                elif not students:
                                        print('\nErro! Não há Alunos cadastrados.')
                                elif any(len(cohort['Alunos']) < 40 for cohort in cohorts):
                                        if any('Turma' not in student for student in students):
                                                students_on_cohort()
                                        else:
                                                print('\nErro! Todos os Estudantes já estão matriculados em alguma Turma.')
                                else:
                                        print('\nErro! Não há nenhuma Turma com vagas.')
                        if option == '9': #Consulta Professor da Disciplina
                                if not disciplines:
                                        print('\nErro! Não há Disciplinas cadastradas.')
                                elif not teachers:
                                        print('\nErro! Não há Professores cadastrados.')
                                else:
                                        consult_teacher_of_disc()
                        if option == '10': #Consulta DIsciplinas do Professor
                                if not disciplines:
                                        print('\nErro! Não há Disciplinas cadastradas.')
                                elif not teachers:
                                        print('\nErro! Não há Professores cadastrados.')
                                else:
                                        consult_discs_of_teacher()
                        if option == '11': #Consulta Alunos de Turma
                                if not students:
                                        print('\nErro! Não há Alunos cadastrados.')
                                elif not teachers:
                                        print('\nErro! Não há Professores cadastrados.')
                                else:
                                        consult_students_of_cohort()
                        if option == '12': #Consulta DIsciplinas da Turma
                                if not disciplines:
                                        print('\nErro! Não há Disciplinas cadastradas.')
                                elif not cohorts:
                                        print('\nErro! Não há Turmas cadastradas.')
                                else:
                                        consult_discs_of_cohort()
                        return True
                else:
                        print('\nOpção inválida. Tente novamente.')

def main_menu_is_comming():
        """main_menu_is_comming: Pausa antes do Menu Principal

        Pausa para usuário poder ler prints finais das funções executadas.
        """
        input('\nVoltando ao MENU PRINCIPAL. Tecle ENTER para prosseguir.')

def the_end():
        """the_end: Fim do programa.

        Comunica encerramento do programa.
        """
        print('\nSistema Acadêmico encerrado.')

def credits():
        """credits: Créditos do programa.

        Apresenta o responsável pela criação do programa.
        """
        print('\nCréditos: Adilson Valentim - Estudante 1º Período de TADS - IFMS Câmpus Três Lagoas - 2024')

title() #Apresenta o título
username = ask_username() #Recebe o nome do usuário
introduction(username) #Apresenta as funcionalidades do Programa
running = True
while running: #Laço que executa o 'Coração' do Programa
        main_menu() # Mostra as Opções
        running = option_executor() # Roda a Opção selecionada e Recebe se continua ou não o Programa
        if running == True: #Continua o Programa
                main_menu_is_comming() # Pausa antes de exibir o MENU PRINCIPAL
        else: #Encerra o Programa
                the_end() #Fim do Programa
                credits() #Créditos

'''
Objetivo de Estrutura de dados:
        Cursos: Nome, Código X####
                Não depende de nada. Usuário INSERE nome. Sistema GERA código. Terminal EXIBE associação
        Turmas: Nome("Nome_do_Curso AAS", onde AA é o ano e S é o Semestre(1 ou 2)), Código X####AAS
                Depende de existir ao menos um CURSO. Terminal EXIBE cursos. Usuário SELECIONA curso. Terminal PERGUNTA ano e semestre da turma.
                Sistema GERA(CONCATENA) código. Terminal EXIBE associação.
        Disciplinas: Nome, Código X#####, Carga Horária(15, 30, 45, 60, 75, 90, 105, 120 H.A)
                Não depende de nada. Usuário INSERE nome e carga horária. Sistema GERA código. Terminal EXIBE associação
        Professores: Nome, Matrícula ######X, Data de Nascimento(Mín 18), Sexo(M, F, NB), Endereço, Telefone, E-mail
                Não depende de nada. Usuário INSERE nome, data de nascimento, sexo, endereço, telefone e e-mail. Sistema GERA matrícula.
                Terminal EXIBE associação
        Alunos: Nome, Matrícula ########X, Data de Nascimento(Mín 18), Sexo(M, F, NB), Endereço, Telefone, E-mail
                Não depende de nada. Usuário INSERE nome, data de nascimento, sexo, endereço, telefone e e-mail. Sistema GERA matrícula
                Terminal EXIBE associação


        Alocar professores em Disciplinas: (Máx 600 Horas (15Semanas*40H))
                Terminal EXIBE professores. Usuário SELECIONA professor. Terminal EXIBE DISCIPLINAS. Usuário SELECIONA disciplina.
                Terminal EXIBE associação e o progresso de Carga Horária Total do professor.
        Alocar Disciplinas em Turmas: (Màx 375 Horas)
                Terminal EXIBE turmas. Usuário SELECIONA turma. Terminal EXIBE disciplinas. Usuário SELECIONA disciplinas.
                Terminal EXIBE associação
        Alocar alunos em Turma: (Máx 40 Alunos / Turma)
                Terminal EXIBE disciplinas. Usuário SELECIONA disciplina. Terminal EXIBE alunos. Usuário SELECIONA alunos.
                Terminal EXIBE associação 


        Filtra o professor de uma dada disciplina
                Terminal SOLICITA código da disciplina ou pergunta se usuário quer a lista de disciplinas. Usuário INSERE código da disciplina
                Terminal EXIBE o professor dessa disciplina
        Filtra as disciplinas de um dado professor
                Terminal SOLICITA código de professor ou pergunta se usuário quer a lista de professores. Usuário INSERE código do professor
                Terminal EXIBE disciplinas do professor
        Filtra os alunos matriculados em dada turma
                Terminal SOLICITA código da turma ou pergunta se usuário quer a lista das turmas. Usuário INSERE código da turma
                Terminal EXIBE os alunos matriculados nessa turma
        Filtra as disciplinas alocadas em dada turma
                Terminal SOLICITA código da turma ou pergunta se usuário quer a lista das turmas. Usuário INSERE código da turma
                Terminal EXIBE as disciplinas dessa turma

Se der tempo:
        Verificar quais disciplinas ainda não possuem professor(?)
        Verificar progresso de carga horária dos professores(?)
        Verificar carga horária disponível para cada turma(?)
        Verificar quantidade de vagas de alunos disponíveis para cada turma(?)
        ?????
'''

'''
POSSÍVEIS FERRAMENTAS:

fake = Faker('pt_BR')


fake.name()
fake.date_of_birth(minimum_age=18, maximum_age=80)
choice(["M", "F", "NB"])
fake.address()
fake.phone_number()
fake.email()
choice([15, 30, 45, 60, 75, 90, 105, 120])

choice(["20", "21", "22", "23", "24", "25"]) #Ano da Turma
choice(["1", "2"]) #Semestre

f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=4, fix_len=True)}"#Código Curso
f"{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{fake.random_number(digits=5, fix_len=True)}"#Código Disciplina
f"{fake.random_number(digits=6, fix_len=True)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"#Matrícula Professores
f"{fake.random_number(digits=8, fix_len=True)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"#Matrícula Alunos


fake.random_element(["Matemática Básica", "Estatística", "Cálculo Diferencial e Integral", "Física Geral", 
"Química Geral", "Comunicação Empresarial", "Gestão de Projetos", "Inglês Técnico", 
"Metodologia Científica", "Ética Profissional", "Sociologia", "Psicologia Organizacional",
"Programação", "Estrutura de Dados", "Banco de Dados", "Engenharia de Software", 
"Redes de Computadores", "Segurança da Informação", "Automação de Processos", 
"Eletrônica Digital", "Mecânica dos Sólidos", "Arquitetura de Computadores", 
"Inteligência Artificial", "Sistemas Embarcados", "Anatomia Humana", "Fisiologia", 
"Microbiologia", "Farmacologia", "Bioquímica Clínica", "Saúde Coletiva", "História Geral", 
"Geografia Econômica", "Literatura Brasileira", "Teoria da Literatura", 
"Pedagogia e Didática", "Educação Inclusiva", "Administração Geral", "Marketing", 
"Gestão de Pessoas", "Contabilidade Geral", "Logística", "Planejamento Estratégico", 
"Empreendedorismo", "Finanças Corporativas", "Gestão de Talentos", 
"Direito Constitucional", "Direito Penal", "Direito Trabalhista", "Ética Jurídica", 
"Processo Penal", "Direito Civil", "Nutrição e Saúde", "Planejamento Urbano", 
"Paisagismo", "Fotografia e Comunicação", "Teorias da Comunicação", 
"Produção de Conteúdo Audiovisual", "Educação Física e Esportes", "Biologia Molecular", 
"Imunologia", "Geopolítica", "Cartografia", "Astronomia", "Robótica"])

fake.random_element(["Matemática Básica", "Estatística", "Cálculo Diferencial e Integral", "Física Geral", "Química Geral", "Comunicação Empresarial", "Gestão de Projetos", "Inglês Técnico", "Metodologia Científica", "Ética Profissional", "Sociologia", "Psicologia Organizacional", 
"Programação", "Estrutura de Dados", "Banco de Dados", "Engenharia de Software", 
"Redes de Computadores", "Segurança da Informação", "Automação de Processos", 
"Eletrônica Digital", "Mecânica dos Sólidos", "Arquitetura de Computadores", 
"Inteligência Artificial", "Sistemas Embarcados", "Anatomia Humana", "Fisiologia", 
"Microbiologia", "Farmacologia", "Bioquímica Clínica", "Saúde Coletiva", "História Geral", 
"Geografia Econômica", "Literatura Brasileira", "Teoria da Literatura", 
"Pedagogia e Didática", "Educação Inclusiva", "Administração Geral", "Marketing", 
"Gestão de Pessoas", "Contabilidade Geral", "Logística", "Planejamento Estratégico", 
"Empreendedorismo", "Finanças Corporativas", "Gestão de Talentos", 
"Direito Constitucional", "Direito Penal", "Direito Trabalhista", "Ética Jurídica", 
"Processo Penal", "Direito Civil", "Nutrição e Saúde", "Planejamento Urbano", 
"Paisagismo", "Fotografia e Comunicação", "Teorias da Comunicação", 
"Produção de Conteúdo Audiovisual", "Educação Física e Esportes", "Biologia Molecular", 
"Imunologia", "Geopolítica", "Cartografia", "Astronomia", "Robótica"])

if __name__ == '__main__':
        main()
'''