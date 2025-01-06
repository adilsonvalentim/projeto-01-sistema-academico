from faker import Faker
from random import choice
from b_courses import registering_courses, courses
from c_cohorts import registering_cohorts, cohorts
from d_disciplines import registering_disciplines, disciplines_on_teacher, disciplines
from e_teachers import registering_teachers, teachers
from f_students import registering_students
from g_util import OperationCancelled

def title():
        print('\n* * * * * SISTEMA ACADÊMICO * * * * *')
        
def ask_username():
        username = input('\nPor favor usuário, insira o seu nome: ')
        return username

def introduction(username):
        print(f'\nOlá {username}, este programa é um Sistema Acadêmico. Nele, você poderá cadastrar Cursos, Turmas, Disciplinas,\n'
                'Professores e Alunos. Também poderá alocar Disciplinas aos Professores, Disciplinas às Turmas e matricular Alunos em Turmas.\n'
                'Por fim, poderá consultar Professores por Disciplinas, Disciplinas por Professores, Alunos por Turmas, Disciplinas por Turmas.\n'
                'Para realizar Cadastros, Alocações, Matrículas e Consultas, você deverá inserir o número correspondente no MENU PRINCIPAL.')
        
def main_menu():
        print('\n* * * MENU PRINCIPAL * * *\n'
                '1 - Cadastrar Curso\n'#ok
                '2 - Cadastrar Turma\n'#ok
                '3 - Cadastrar Disciplina\n'#ok
                '4 - Cadastrar Professores\n'#ok
                '5 - Cadastrar Alunos\n'#ok
                '6 - Alocar Disciplinas a Professor\n'#Construido em Disciplinas
                '7 - Alocar Disciplinas a Turma\n' #Construido em Disciplinas
                '8 - Matricular Aluno em Turma\n'
                '9 - Consultar Professor por Disciplina\n'
                '10 - Consultar Disciplinas por Professor\n'
                '11 - Consultar Alunos por Turma\n'
                '12 - Consultar Disciplinas por Turma\n'
                'sair - Encerra o Programa')

def choose_function():
        option = 0
        option = input('\nPor favor, insira o número da função que deseja executar: ')
        return option

def option_executor(option):
        if option == '1':
                return registering_courses()
        if option == '2':
                if courses:
                        return registering_cohorts()
                print('\nErro! Cadastre algum Curso antes de cadastrar alguma Turma.')
        if option == '3':
                return registering_disciplines()
        if option == '4':
                return registering_teachers()
        if option == '5':
                return registering_students()
        if option == '6':
                if any('Professor' not in discipline for discipline in disciplines):
                        if teachers:
                                return disciplines_on_teacher()
                        print('\nErro! Cadastre algum Professor antes de alocar Disciplinas a Professor.')
                print('\nErro! Não há Disciplinas disponíveis para alocação de Professor.'
                        '\nCadastre uma nova Disciplina, e tente novamente.')
        if option == '7':
                if any('Turma' not in discipline for discipline in disciplines):
                        if cohorts:
                                return disciplines_on_teacher()
                        print('\nErro! Cadastre alguma Turma antes de alocar Disciplinas a Turma.')
                print('\nErro! Não há Disciplinas disponíveis para alocação em Turma.'
                        '\nCadastre uma nova Disciplina, e tente novamente.')
                
        
running = True
while running:
        try:
                main_menu()
                option = choose_function()
                option_executor(option)
                
        except OperationCancelled:
                print('\nVoltando ao MENU PRINCIPAL.')
        

'''Estrutura de dados:
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
        Alocar alunos em Turma: (Máx 60 Alunos / Turma)
                Terminal EXIBE disciplinas. Usuário SELECIONA disciplina. Terminal EXIBE alunos. Usuário SELECIONA alunos.
                Terminal EXIBE associação 
        
        
        Filtra as disciplinas de um dado professor
                Terminal SOLICITA código de professor ou pergunta se usuário quer a lista de professores. Usuário INSERE código do professor
                Terminal EXIBE disciplinas do professor
        Filtra o professor de uma dada disciplina
                Terminal SOLICITA código da disciplina ou pergunta se usuário quer a lista de disciplinas. Usuário INSERE código da disciplina
                Terminal EXIBE o professor dessa disciplina
        Filtra os alunos matriculados em dada turma
                Terminal SOLICITA código da turma ou pergunta se usuário quer a lista das turmas. Usuário INSERE código da turma
                Terminal EXIBE os alunos matriculados nessa turma
        Filtra as disciplinas alocadas em dada turma
                Terminal SOLICITA código da turma ou pergunta se usuário quer a lista das turmas. Usuário INSERE código da turma
                Terminal EXIBE as disciplinas dessa turma
                
        Verificar quais disciplinas ainda não possuem professor(?)
        Verificar progresso de carga horária dos professores(?)
        Verificar carga horária disponível para cada turma(?)
        Verificar quantidade de vagas de alunos disponíveis para cada turma(?)
        
        
        
        
        '''
                
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