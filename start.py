'''import util
util.minha_funcao()'''

'''from util import minha_funcao
minha_funcao'''

from faker import Faker
from random import choice
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
        Alocar alunos em Turma: (Máx 60 Alunos / Turma)
                Terminal EXIBE disciplinas. Usuário SELECIONA disciplina. Terminal EXIBE alunos. Usuário SELECIONA alunos.
                Terminal EXIBE associação 
        Alocar Disciplinas em Turmas: (Màx 375 Horas)
                Terminal EXIBE turmas. Usuário SELECIONA turma. Terminal EXIBE disciplinas. Usuário SELECIONA disciplinas.
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
                Terminal EXIBE as disciplinas dessa turma'''
                
fake = Faker('pt_BR')


fake.name()
fake.date_of_birth(minimum_age=18, maximum_age=80)
choice(["M", "F", "NB"])
fake.address()
fake.phone_number()
fake.email()
choice([15, 30, 45, 60, 75, 90, 105, 120])

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