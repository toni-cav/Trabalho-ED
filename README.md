# 📚 Guia Rápido para Trabalhar com Git

Este documento tem como objetivo padronizar o fluxo de trabalho da equipe e evitar conflitos durante o desenvolvimento.

---

## 1️⃣ Clonar o repositório

Abra o terminal na pasta onde deseja salvar o projeto e execute:

```bash
git clone LINK_DO_REPOSITORIO
```

Após clonar:

```bash
cd nome-do-projeto
```

---

## 2️⃣ Criar sua própria branch

**Nunca trabalhe diretamente na branch `main`.**

Cada integrante deve criar sua própria branch para desenvolver suas funcionalidades ou correções.

```bash
git checkout -b nome-da-branch
```

### Exemplos

```bash
git checkout -b antonio
git checkout -b feature/login
git checkout -b fix/erro-validacao
```

---

## 3️⃣ Atualizar o projeto antes de começar

Antes de iniciar qualquer desenvolvimento, sincronize sua cópia local com a versão mais recente do projeto:

```bash
git pull origin main
```

Isso evita conflitos e garante que você esteja trabalhando na versão mais atual.

---

## 4️⃣ Verificar arquivos alterados

```bash
git status
```

Este comando mostra:

- Arquivos modificados
- Arquivos novos
- Arquivos prontos para commit
- Arquivos ainda não adicionados

---

## 5️⃣ Adicionar alterações

Adicionar todos os arquivos modificados:

```bash
git add .
```

Adicionar um arquivo específico:

```bash
git add nome_do_arquivo.py
```

Após executar o `git add`, suas alterações estarão prontas para serem registradas em um commit.

---

## 6️⃣ Criar um commit

```bash
git commit -m "descrição da alteração"
```

### Exemplos

```bash
git commit -m "feat: adiciona filtro por data"
git commit -m "fix: corrige validação de usuário"
git commit -m "refactor: reorganiza estrutura do serviço"
```

### Convenção de commits

| Prefixo | Descrição |
|----------|------------|
| feat | Nova funcionalidade |
| fix | Correção de bug |
| refactor | Refatoração de código |
| docs | Alteração de documentação |
| test | Inclusão ou ajuste de testes |
| chore | Ajustes gerais e manutenção |

---

## 7️⃣ Enviar alterações para o GitHub

### Primeiro envio da branch

```bash
git push -u origin nome-da-branch
```

### Próximos envios

```bash
git push
```

---

## 8️⃣ Atualizar sua branch com mudanças da main

Caso outras pessoas tenham realizado alterações:

```bash
git pull origin main
```

---

## ⚠️ Regras Importantes

- ❌ Não trabalhar diretamente na `main`
- ✅ Sempre criar uma branch própria
- ✅ Fazer commits pequenos e organizados
- ✅ Atualizar o projeto antes de começar (`git pull`)
- ✅ Utilizar mensagens de commit descritivas
- ✅ Enviar alterações frequentemente para evitar perdas

---

## 📌 Comandos Úteis

### Ver todas as branches

```bash
git branch
```

### Trocar de branch

```bash
git checkout nome-da-branch
```

### Criar e trocar para uma branch

```bash
git checkout -b nova-branch
```

### Renomear a branch atual

```bash
git branch -m novo-nome
```

> ⚠️ É necessário estar na branch que deseja renomear.

### Desfazer alterações locais

```bash
git restore .
```

### Atualizar e voltar exatamente para o remoto

```bash
git fetch
git reset --hard origin/main
```

> ⚠️ Este comando remove todas as alterações locais não enviadas.

---

## 🌱 Padrão de Nomes para Branches

### Novas funcionalidades

```text
feature/nome-da-funcionalidade
```

Exemplos:

```text
feature/filtros-planilha
feature/autenticacao
feature/exportacao-pdf
```

### Correções

```text
fix/nome-da-correcao
```

Exemplos:

```text
fix/erro-validacao
fix/tratamento-excecao
```

### Refatorações

```text
refactor/nome-da-refatoracao
```

Exemplos:

```text
refactor/processamento-dados
```

---

## 📝 Padrão de Commits

### Funcionalidades

```bash
git commit -m "feat: adiciona exportação para PDF"
```

### Correções

```bash
git commit -m "fix: corrige validação de login"
```

### Refatorações

```bash
git commit -m "refactor: melhora organização do código"
```

### Documentação

```bash
git commit -m "docs: atualiza README"
```

### Testes

```bash
git commit -m "test: adiciona testes do módulo de usuários"
```

---

## ✅ Fluxo Recomendado

```bash
git pull origin main

git checkout -b minha-branch

# Desenvolver

git add .

git commit -m "feat: minha alteração"

git push -u origin minha-branch
```

Seguindo este fluxo, conseguimos trabalhar em equipe de forma organizada, reduzir conflitos e manter o histórico do projeto limpo e fácil de entender.
