from metodos import clear, cadastrarContato, verificarArquivos, listarContatos, deletarContato, atualizarContato
from time import sleep
import os
os.makedirs('data', exist_ok=True)

def main():
    rodar = True
    
    while(rodar):
        dadosSalvos = verificarArquivos()
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
                contato = cadastrarContato(False)
                contatoTemp = contato.replace(";"," ")
                contatoTemp = contatoTemp.split()
                telefone = contato[2]
                email = contato[3]
                try:
                    with open('data/contatos.txt', 'a') as arquivo:
                        if telefone in dadosSalvos:
                            print("Telefone Repetido")
                        elif email in dadosSalvos:
                            print("Email Repetido")
                        else:
                            arquivo.write(contato)

                except FileNotFoundError:
                    with open('data/contatos.txt', 'w') as arquivo:
                        if telefone in dadosSalvos:
                            print("Telefone Repetido")
                        elif email in dadosSalvos:
                            print("Email Repetido")
                        else:
                            arquivo.write(contato)
            case 2:
                listaFormatada = listarContatos(dadosSalvos)
                print("\n".join(sorted(listaFormatada)))
                input()

            case 3:
                encontrou = False
                busca = input("Insira nome ou telefone: ")
                
                if busca.isalpha():
                    busca = busca.strip()
                
                for linha in dadosSalvos:
                    buscaTemp = linha.lower()
                    if busca in buscaTemp:
                        print(linha)
                        encontrou = True
                if not encontrou:
                    print("Busca não encontrada")
                input()

            case 4:
                email = input("Digite o email da pessoa a atualizar: ")
                atualizou = atualizarContato(dadosSalvos,email)
                if atualizou:
                    print("Contato Atualizado")
                    sleep(3)
                else:
                    print("Email não encontrado")
                    sleep(3)

            case 5:
                telefone = input("Telefone do cadastro a ser deletado: ")
                deletou = deletarContato(dadosSalvos, telefone)
                if deletou:
                    print("Contato Deletado")
                    sleep(3)
                else:
                    print("Contato não encontrado")
                    sleep(3)
                    
            case 6:
                listaExportada = ""
                for linha in dadosSalvos:
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