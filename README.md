# 📌 API Simples com FastAPI

Ele cobre três operações básicas de um CRUD:\
- **GET /usuarios** --- listar usuários\
- **POST /usuarios** --- criar usuário\
- **DELETE /usuarios/{id}** --- remover usuário

Os dados são armazenados **em memória** (lista Python).\
⚠️ Isso significa que toda vez que reiniciar o servidor, a lista de
usuários será zerada.

------------------------------------------------------------------------

## 🛠️ Requisitos

-   Python 3.8+
-   Navegador web (para abrir o `index.html`)

------------------------------------------------------------------------

## 📦 Instalação e execução

### 1. Criar ambiente virtual

``` bash
python -m venv venv
```

Ativar venv:\
- **Windows**: `venv\Scripts\activate`\
- **Linux/Mac**: `source venv/bin/activate`

### 2. Instalar dependências

``` bash
pip install fastapi uvicorn
```

### 3. Rodar a API

``` bash
python -m uvicorn main:app --reload
```

A API rodará em: <http://127.0.0.1:8000>\
A documentação automática do FastAPI estará em:
<http://127.0.0.1:8000/docs>

### 4. Abrir o frontend

Abra o arquivo `index.html` no navegador (duplo clique).

---

## 📚 Explicação do código

### Backend (FastAPI)

-   **`usuarios = []`** → lista em memória que guarda os usuários.\
-   **Classe `Usuario` ** → define a estrutura de um usuário
    (`id`, `nome`, `idade`).\
-   **`@app.get("/usuarios")`** → retorna a lista completa.\
-   **`@app.post("/usuarios")`** → recebe JSON no corpo da requisição,
    adiciona à lista e retorna confirmação.\
-   **`@app.delete("/usuarios/{usuario_id}")`** → procura pelo ID e
    remove da lista; se não encontrar, retorna mensagem de erro.\
-   **CORS** → necessário para permitir que o navegador (HTML local)
    consiga chamar a API sem bloqueio.

### Frontend (HTML + JS)
---
-   **Botões e inputs** → usados para acionar funções JS.\
-   **Cada input tem um id usado pelo JavaScript para ler o valor.** 
-   **`fetch`** → responsável por fazer requisições AJAX:
    -   `fetch('/usuarios')` com método padrão `GET`.\
    -   `fetch('/usuarios', { method: 'POST', body: JSON.stringify(...) })`
        para criar.\
    -   `fetch('/usuarios/{id}', { method: 'DELETE' })` para deletar.\
-   **`document.getElementById(...).value`** → lê valores dos inputs.\
-   **`JSON.stringify(dados, null, 2)`** → exibe JSON de forma formatada
    no `<pre>`.\
-   **`alert(dados.mensagem)`** → mostra mensagens de retorno (sucesso
    ou erro).

------------------------------------------------------------------------

## ⚠️ Observações

-   O projeto é **didático** (CRD básico com lista em memória).\
-   Dados **não são persistidos** (se reiniciar a API, tudo é apagado).\
-   CORS liberado para qualquer origem (`"*"`), apenas para
    aprendizado.\
    Em produção, restrinja para domínios confiáveis.\
-   Não há validação de duplicados (se criar dois usuários com o mesmo
    `id`, ambos serão armazenados).



# crd-simples
API simples em FastAPI desenvolvida para estudo, com endpoints de cadastro, listagem e remoção.
