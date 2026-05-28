GUIA PARA TRABALHAR COM O GIT 

1. Clonar o repositório

Abra o terminal na pasta onde deseja salvar o projeto e execute:

git clone LINK_DO_REPOSITORIO
#============================================================================

2. Criar sua própria branch

Cada pessoa deve trabalhar em uma branch separada, assim não sobrepomos nossas mudanças e cada um pode trabalhar tranquilo.

Crie uma branch com seu nome ou com a funcionalidade:

git checkout -b nome-da-branch

Exemplos:

git checkout -b antonio
git checkout -b feature-login
git checkout -b correcao-api
#============================================================================

3. Atualizar o projeto antes de começar

Antes de mexer no código, atualize o projeto:

git pull origin main



4. Verificar arquivos alterados
git status

git status vai te mostrar tudo o que foi alterado para voce poder fazer o commit

5. Adicionar arquivos modificados

Adicionar tudo:

git add .

Ou adicionar um arquivo específico:

git add nome_do_arquivo.py

Isso é para confirmar as mudanças que voce fez na sua branch, assim que voce confirma esta pronto para fazer o commit

6. Fazer commit
git commit -m "descrição da alteração"

Exemplos:

git commit -m "feat: adiciona função de filtros"
git commit -m "fix: corrige erro de validação"

*Irei colocar uma tabelinha de como fazer os commits e os nomes das branchs para ficarmos mais organizados
*
7. Enviar alterações para o GitHub

Primeira vez na branch:

git push -u origin nome-da-branch

Depois:

git push


8. Atualizar sua branch com mudanças do projeto

Caso alguém altere o projeto:

git pull origin main

⚠️ Regras Importantes
° NÃO trabalhar direto na master/main
° Sempre criar uma branch
° Fazer commits pequenos e organizados
° Antes de começar, usar git pull
°Tentar escrever commits descritivos


📌 Comandos Úteis
Ver branches
    git branch

Trocar de branch
    git checkout nome-da-branch

Criar branch e trocar ao mesmo tempo
    git checkout -b nova-branch

Voltar alterações locais
    git restore .

Atualizar e resetar tudo para o remoto
    git fetch
    git reset --hard origin/master
Cuidado: isso apaga alterações locais.

Troca nome da branch
    git branch -m nome-novo
Cuidado: Tem que estar dentro da branch que quer mudar o nome

🧠 Sugestão de nomes de branch
Funcionalidades
feature/nome

Exemplo:

feature/filtros-planilha
Correções
fix/nome

Exemplo:

fix/erro-validacao
✅ Fluxo recomendado
git pull
git checkout -b minha-branch


# faz alterações
git add .
git commit -m "feat: minha alteração"
git push -u origin minha-branch