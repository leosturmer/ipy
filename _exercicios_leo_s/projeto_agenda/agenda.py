
"""
Model da Agenda
Autor: Leonardo Stürmer
Data: 16/05/2025

"""

minha_agenda = {}

def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    status = False
    if email not in agenda.keys():
        agenda[email] = [nome, idade, endereco, favorito]
        status = True
    
    return (status, email)

def atualizar(agenda, email, nome, idade, endereco, favorito=False):
    status = True

    try:
       agenda[email] = [nome, idade, endereco, favorito] 
       
    except KeyError:
        status = False
    
    return (status, email)

def favoritar(agenda, email):
    status = True
    try:
        agenda[email][3] = True
    except KeyError:
        status = False
        
    return (status, email)

def apagar(agenda, email):
    status = True
    try:
        del agenda[email]
    except KeyError:
        status = False
    
    return (status, email)

"""
def consultar(agenda, email):
    try:
        return agenda[email]
    except KeyError:
        return None
"""

def consultar(agenda, email):
    status = True
    dados = []
    try: 
        dados = agenda[email]
    except KeyError:
        status = False
    return(status, dados)

def agenda_init():
    cadastrar(minha_agenda, 'leo@leo.com', 'Leo S', 29, 'Rua X')
    cadastrar(minha_agenda, 'leo2@leo.com', 'Leo 2S', 30, 'Rua 2X', True)
    cadastrar(minha_agenda, 'leo3@leo.com', 'Leo 3S', 31, 'Rua 3X')

"""
View da Agenda

"""

def imprimir(registros):
    for email, dados in registros:
        print(f'''e-mail:{email}
    Nome: {dados[0]}
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}
        ''')

def imprimir_um(registro):
    email, dados = registro
    print(f'''e-mail:{email}
    Nome: {dados[0]}
    Endereço: {dados[2]}
    Idade: {dados[1]}
    Favorito: {dados[3]}
    ''')

  
"""
Controlador da Agenda

"""

agenda_init()

print("Agenda 2025 (CLI) - v.0.1.0 - Senac Tech = POA/RS")

# inicia o uso do sistema


# recebe dados da View 
email = "leo@leo.com" # deveria ser um input() aqui

# consultar model - consultar()
registros = consultar(minha_agenda, email)

if registros:
    # repassar os dads da View os dados obtidos pela Model
    imprimir_um((email, registros))
else:
    print("Registro não encontrdo")

sucesso = apagar(minha_agenda, "leo2leo.com")
if sucesso:
    print("Registro Excluído")
else:
    print("Registro inexistente")
