# Testes do Sistema

## Cenários de testes

### Requisito Funcional RF 01 - Cadastro de informações:

Cenário de teste: Usuário cadastra informações válidas.

Passos:
1. Acessar o site.
2. Preencher o formulário de cadastro com informações válidas.
3. Enviar o formulário.

Resultado esperado:
- As informações são salvas no banco de dados.
- Uma mensagem de sucesso é exibida.

### Requisito Funcional RF 02 - Validação de informações:

Cenário de teste: Usuário cadastra informações inválidas.

Passos:
1. Acessar o site.
2. Preencher o formulário com informações inválidas.
3. Enviar o formulário.

Resultado esperado:
- O sistema identifica as inconsistências e exibe mensagens de erro apropriadas.

### Requisito Funcional RF 03 - Tela inicial com informações cadastradas:

Cenário de teste: Exibição dos produtos existentes na loja na tela inicial.

Passos:
1. Acessar o site.

Resultado esperado:
- A tela inicial exibe corretamente as informações cadastradas.
- As informações são recuperadas do banco de dados.

### Requisito Funcional RF 04 - Compra de produto:

1. Cenário de teste: Usuário adiciona um produto ao carrinho e conclui a compra.

Passos:
1. Acessar o site.
2. Selecionar um item e adicionar ao carrinho de compras.
3. Clicar no ícone do carrinho de compras.
4. Verificar a quantidade e o valor total dos itens.
5. Clicar em "Prosseguir".
6. Preencher os dados de pagamento.
7. Clicar em "Finalizar compra".

Verificações:
- A compra é registrada no banco de dados.
- Uma mensagem de sucesso é exibida.

## Testes unitários e de integração

Os testes unitários e de integração da loja virtual foram realizados utilizando o framework de testes `pytest`.

Testamos as seguintes rotas:

- `GET /users`: Deve retornar uma lista de todos os usuários do banco de dados.
- `GET /users/<int:user_id>`: Deve retornar as informações do usuário com o ID especificado.
- `POST /users`: Deve adicionar um novo usuário ao banco de dados.
- `PUT /users/<int:user_id>`: Deve atualizar o usuário com o ID especificado.
- `DELETE /users/<int:user_id>`: Exclui o usuário com o ID especificado.
- `GET /produtos`: Retorna uma lista de todos os produtos do banco de dados.
- `GET /products/<int:product_id>`: Retorna o produto com o ID especificado.
- `POST /products`: Adiciona um novo produto ao banco de dados.
- `PUT /products/<int:product_id>`: atualiza o produto com o ID especificado.

Notamos que na nossa aplicação o conceito de teste unitário acaba envolvendo o de teste de integração, pois a maioria das funções depende de outras funções para funcionar corretamente. Por exemplo, não é possível obter os usuários sem requisitar as informações para o banco de dados.

Os testes estão no arquivo da pasta `sprint_4_codigo_mvp/backend/store-microsservice/test_app.py`, e podem ser executados com o comando `python test_app.py`. É necessário preencher as informações de um banco de dados na RDS (endpoint, username, senha e nome do banco) no arquivo `app.py`.

## Testes de microsserviços

Elaboramos um microsserviço em Node.js que simula um serviço de pagamento. O microsserviço recebe um JSON com as informações do pagamento e retorna um JSON com o status da transação (aprovado ou reprovado), dependendo da rota usada.

Os testes de microsserviços foram realizados utilizando o framework `jest`. Os testes estão no arquivos na pasta `sprint_4_codigo_mvp/backend/payment-microsservice/spec/` e podem ser executados com o comando `npm run test`.

Foram testadas as seguintes rotas:

- `GET /approvePayment`: Retorna um JSON com o status da transação aprovado.
- `GET /rejectPayment`: Retorna um JSON com o status da transação reprovado.
