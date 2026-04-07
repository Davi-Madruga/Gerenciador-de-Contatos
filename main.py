from metodos import verificarArquivos,cadastrarContato,listarContatos,buscarContato,deletarContato, atualizarContato, clear
from time import sleep
import os
os.makedirs('data', exist_ok=True)

def main():
    rodar = True
    
    while(rodar):
        contatos = verificarArquivos()
        clear()
        print("""
-------- MENU --------
[1] Adicionar contato
[2] Listar contatos
[3] Buscar contato
[4] Atualizar contato
[5] Deletar contato
[6] Exportar contatos
[7] Sair """)
        try: 
            opcao = int(input("-> "))
        except ValueError:
            print("erro")
            continue
        match opcao:
            case 1:
                cadastrado = cadastrarContato(True,contatos)
                print("Contato Cadastrado") if cadastrado else print("Contato NÃO Cadastrado")
                sleep(3)

            case 2:
                listaFormatada = listarContatos(contatos)
                print(listaFormatada)
                input("Pressione qualquer tecla...")

            case 3:
                listaBusca = buscarContato(contatos)
                if listaBusca:
                    print(listarContatos(listaBusca))
                    input("Pressione qualquer tecla...")
                else: 
                    print("Busca não encontrada")
                    sleep(3)
                
            case 4:
                email = input("Digite o email da pessoa a atualizar: ")
                atualizou = atualizarContato(contatos,email)
                if atualizou:
                    print("Contato Atualizado")
                    sleep(3)
                else:
                    print("Email não encontrado")
                    sleep(3)

            case 5:
                telefone = input("Telefone do cadastro a ser deletado: ")
                deletou = deletarContato(contatos, telefone)
                if deletou:
                    print("Contato Deletado")
                    sleep(3)
                else:
                    print("Contato não encontrado")
                    sleep(3)
                    
            case 6:
                listaExportada = ""
                for linha in contatos:
                    linha = linha.replace(';', ' ')
                    linha = linha.split()
                    listaExportada += f"Nome: {linha[0]} {linha[1]}\n"
                    listaExportada += f"Telefone: {linha[2]}\n"
                    listaExportada += f"Email: {linha[3]}\n"

                with open('data/export_contatos.txt', 'w') as arquivo:
                    arquivo.write(listaExportada)
                print("Lista Exportada")
                sleep(3)

            case 7:
                print("Fechando programa...")
                rodar = False
            case _:
                print("erro")

if __name__ == '__main__':
    main()