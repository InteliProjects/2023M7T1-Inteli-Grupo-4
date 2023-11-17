# Especificação de Requisitos

## Requisitos funcionais

## Cadastro de informações

Esses requisitos funcionais estão relacionados com o MVP desenvolvido na Sprint 1 (CRUD Básico).

### RF 01

O sistema deve permitir que os usuários cadastrem informações no site, através de um formulário HTML (C do CRUD - "Create, Read, Update, Delete").

### RF 02

O sistema deve identificar inconsistências nas informações fornecidas durante o processo de cadastro, com uma etapa inicial de validação no front-end e outra no back-end, quando salvar os registros no banco de dados.

### RF 03

O sistema deve mostrar uma tela inicial com as informações já cadastradas (R do CRUD).

### RF 04

O sistema deve permitir que os usuários editem e excluam as informações já cadastradas na aplicação (U e D do CRUD).

## Planos e serviços

Esses requisitos funcionais estão relacionados com o MVP que será desenvolvido nas Sprints 2 e seguintes.

### RF 05

O sistema deve apresentar diferentes planos de serviço de máquina de cartão, e outros serviços.

### RF 06

O sistema deve permitir que os usuários escolham o plano adequado às suas necessidades.

### RF 07

O sistema deve  permitir que o usuário escolha o plano antes de realizar cadastro no sistema.

## Suporte ao cliente

### RF 08

O sistema deve  disponibilizar um canal de suporte ao cliente, como chat ao vivo, e-mail ou telefone, para auxiliar os usuários com dúvidas, problemas técnicos ou questões relacionadas a pagamentos.

## Cancelamento

### RF 09

O sistema deve  permitir que os usuários solicitem o cancelamento de serviços, com instruções claras sobre o processo.

### RF 10

O sistema deve  facilitar o processo de reembolso em caso de devolução ou problemas com transações.

## Requisitos Não-funcionais

Esses requisitos não-funcionais serão validados através do sistema secundário de teste de carga e estão descritos de acordo com a norma ISO 25010.

## Desempenho

### RNF 01

O tempo de resposta não deve exceder 1 segundo, garantindo uma experiência rápida e eficiente para os usuários.

#### Plano de teste

* Enviar uma série de solicitações simulando ações do usuário e medir o tempo de resposta.

## Confiabilidade

### RNF 02

O sistema deve ser capaz de lidar com um aumento significativo no tráfego durante períodos de pico, como por exemplo, dias de votação do BBB.

#### Plano de teste

* Simular um aumento de tráfego, gradualmente aumentando a carga até o limite e monitorando o desempenho.
* Simular os eventos e cenários com a hospedagem do sistema na nuvem.

### RNF 03

A aplicação deve ser hospedada na Amazon Web Services (AWS), utilizando os serviços de nuvem oferecidos pela plataforma.

#### Plano de teste

* Implantar a aplicação na AWS e verificar se a infraestrutura está configurada corretamente.

## Segurança

### RNF 04

O sistema deve seguir rigorosos padrões de segurança de dados, como o PCI DSS (Padrão de Segurança de Dados do Setor de Cartões de Pagamento), para proteger informações sensíveis de cartão de crédito e dados pessoais dos clientes.

#### Plano de teste

*  Verificar se as medidas de segurança, como criptografia de dados, estão implementadas conforme o PCI DSS.

## Privacidade

### RNF 05

As informações pessoais dos clientes devem ser tratadas com confidencialidade e protegidas contra acesso não autorizado.

#### Plano de teste

*  Tentar acessar informações pessoais sem as devidas permissões.


#### Vídeo com as boas práticas

URL: https://youtu.be/eoM7pDScZpo
