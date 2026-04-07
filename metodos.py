def verificarArquivos():
    try:
        with open('data/contatos.txt', 'r') as arquivo:
            dados = [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        dados = []
    return dados

def cadastrarContato(cadastrar,contatos):
    nome = verificarNome()
    telefone = verificarTelefone()
    email = verificarEmail()
    if cadastrar:
        contato = f"{nome};{telefone};{email}\n"
        modoEscrita = 'a'
        while(1):
            try:
                with open('data/contatos.txt', modoEscrita) as arquivo:
                    if telefone in contatos:
                        print("Telefone Repetido")
                    elif email in contatos:
                        print("Email Repetido")
                    else:
                        arquivo.write(contato)
                        return True
            except FileNotFoundError:
                modoEscrita = 'w'
    else:
        return f"{nome};{telefone};{email}"

def verificarNome():
    while(1):

        nome = input("Nome: ")
        nome = nome.split()
        nome[0] = nome[0].capitalize()

        try:
            nome[1] = nome[1].capitalize()
            if nome[0].isalpha() and nome[1].isalpha():
                nome = f"{nome[0]} {nome[1]}"
                return nome
            print("Insira um nome e sobrenome válido!")

        except IndexError:
            print("Insira um nome e sobrenome válido!")

def verificarTelefone():
    while(1):
        ddds_brasil = [
    '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '21', '22', '24', '27', '28',
    '31', '32', '33', '34', '35', '37', '38',
    '41', '42', '43', '44', '45', '46',
    '47', '48', '49',
    '51', '53', '54', '55',
    '61', '62', '63', '64', '65', '66', '67',
    '68', '69',
    '71', '73', '74', '75', '77',
    '79',
    '81', '82', '83', '84', '85', '86', '87', '88', '89',
    '91', '92', '93', '94', '95', '96', '97', '98', '99'
]
        telefone = input("Telefone: ")             
        if len(telefone) >= 10 and telefone.isnumeric() and f'{telefone[0]}{telefone[1]}' in ddds_brasil:
            return telefone
        else:
            print("Insira um telefone válido!")

def verificarEmail():
    while(1):
        email = input("Email: ")
        if '@' in email and f"{email[-4]}{email[-3]}{email[-2]}{email[-1]}" == ".com":
            email = email.lower()
            return email
        else:
            print("Insira um email válido!")

def listarContatos(contatos):
    contatosFormatados = []

    for contato in contatos:
        contato = contato.split(";")
        contatoFormatado = f"{contato[0]} | {contato[1]} | {contato[2]}"
        contatosFormatados.append(contatoFormatado)

    return "-"*40 + "\n" + "\n".join(sorted(contatosFormatados)) + "\n" + "-"*40

def buscarContato(contatos):
    listaBusca = []
    if contatos:
        busca = input("Insira nome ou telefone: ")

        for contato in contatos:
            contatoTemp = contato.split(";")
            if busca in contatoTemp[0] or contatoTemp[1] == busca:
                listaBusca.append(contato)

    return listaBusca

def atualizarContato(contatos):
    emailEncontrado = False
    email = input("Digite o email da pessoa a atualizar: ")
    email = email.strip().lower()
    
    for i in range(len(contatos)):
        contato = contatos[i]
        contatoTemp = contato.split(";")

        if email == contatoTemp[2]:
            contatos[i] = cadastrarContato(False, contatos)
            emailEncontrado = True
            break

    if emailEncontrado:
        with open(f'data/contatos.txt', 'w') as arquivo:
            for contato in contatos:
                arquivo.write(f'{contato}\n')
    return emailEncontrado

def deletarContato(contatos):
    contatoEncontrado = False

    telefone = input("Telefone do cadastro a ser deletado: ")
    telefone = telefone.strip()
    
    for contato in contatos:
        contatoTemp = contato.split(";")
        if telefone == contatoTemp[1]:
            contatos.remove(contato)
            contatoEncontrado = True
            break
        
    if contatoEncontrado:
        with open(f'data/contatos.txt', 'w') as arquivo:
            for contato in contatos:
                arquivo.write(f'{contato}\n')
        
    return contatoEncontrado

def exportarContatos(contatos):
    listaExportada = ""
    for contato in contatos:
        contato = contato.split(';')
        listaExportada += f"Nome: {contato[0]}\n"
        listaExportada += f"Telefone: {contato[1]}\n"
        listaExportada += f"Email: {contato[2]}\n\n"

    with open('data/export_contatos.txt', 'w') as arquivo:
        arquivo.write(listaExportada)

def clear():
    import os
    os.system("cls")