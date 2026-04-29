# Projeto QA — Automação de Testes

Automação de testes de API e Web desenvolvida como trabalho prático da disciplina de QA.

## Tecnologias

- **API:** Postman + Newman + GitHub Actions
- **Web:** Python, Selenium, Pytest, Page Object Model
- **CI/CD:** GitHub Actions

## Como Executar Localmente

### Testes de API
```bash
npm install -g newman
newman run api-tests/petstore_collection.json --reporters cli
```

### Testes Web
```bash
cd web-tests
pip install -r requirements.txt
pytest tests/ -v
```

## Cenários Cobertos

### API — Swagger Petstore
- Criar usuário
- Buscar usuário
- Listar pets disponíveis
- Criar pet
- Buscar inventário da loja
- Fazer pedido

### Web — SauceDemo
- Login com credenciais válidas
- Login com credenciais inválidas
- Fluxo E2E: login → produto → checkout → confirmação