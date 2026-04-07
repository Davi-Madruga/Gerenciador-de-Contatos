📌 Desafio: Gerenciador de Contatos (Avançado)

🎯 Objetivo:
Criar um sistema em console para gerenciar contatos com persistência em arquivos e validações robustas.

📋 Menu
1 - Adicionar contato
2 - Listar contatos
3 - Buscar contato
4 - Atualizar contato
5 - Deletar contato
6 - Exportar contatos
7 - Sair

📁 Armazenamento
Arquivo: data/contatos.txt
Formato:
Nome;Telefone;Email

Ex:

João Silva;83999999999;joao@email.com
Maria Souza;83988888888;maria@email.com

✏️ Regras de Inserção
TEM QUE PERGUNTAR O NOME COMPLETO (LUIS OUVIU?????)
Sanitizar:
Nome → Primeira letra maiúscula
Email → minúsculo
Telefone → apenas números

❌ Não permitir:

Nome vazio
Nome sem sobrenome
Telefone com menos de 10 dígitos
Email inválido (sem @)
Telefones duplicados
Emails duplicados

🔄 Atualização
Permitir editar:
Nome
Telefone
Email
Validar tudo novamente
Não pode gerar duplicidade

🔍 Busca
Por nome (parcial, case insensitive)
Por telefone

🗑️ Deleção
Usar telefone como identificador
✔ Se existir → remove
❌ Se não existir → erro

📊 Listagem
Exibir:
Nome | Telefone | Email
Ordenado por nome (A-Z)

📤 Exportação
Arquivo: data/export_contatos.txt

Formato:

Nome: João Silva
Telefone: 83999999999
Email: joao@email.com

🔁 Regras Gerais
Menu em loop até sair
Criar /data automaticamente
Tratar erros de leitura/escrita
Sempre mostrar feedback ao usuário

🔐 Regras Avançadas
Nome deve ter pelo menos 2 palavras
Validar DDD do telefone
Email deve seguir padrão básico

🚀 Extras (Opcional)
Paginação na listagem
Edição interativa
Índice por telefone (map)
Log de operações (log.txt)
Backup automático antes de alterações
