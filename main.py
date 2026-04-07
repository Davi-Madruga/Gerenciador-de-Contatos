from metodos import verificarArquivos,cadastrarContato,listarContatos,buscarContato,deletarContato, atualizarContato, exportarContatos, clear
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
                atualizou = atualizarContato(contatos)
                print("Contato Atualizado") if atualizou else print("Email não encontrado")
                sleep(3)

            case 5:
                deletou = deletarContato(contatos)
                print("Contato Deletado") if deletou else print("Contato não encontrado")
                sleep(3)
                 
            case 6:
                exportarContatos(contatos)
                print("Lista de contatos exportada!")
                sleep(3)
                
            case 7:
                print("Fechando programa...")
                rodar = False
            case _:
                print("erro")

if __name__ == '__main__':
    main()