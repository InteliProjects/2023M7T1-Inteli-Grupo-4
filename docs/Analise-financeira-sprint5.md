# Análise de Gestão de Custo

## Introdução

Neste relatório, apresentamos uma análise financeira atualizada do projeto "Aplicação escalável em sistemas distribuídos". A análise considera a evolução da arquitetura da versão 2 (v2) para a versão 5 (V5) e inclui informações críticas sobre custos em momentos de alto índice de acesso. O objetivo é fornecer uma visão abrangente dos custos envolvidos na execução do projeto e avaliar as vantagens de cada componente da arquitetura.

## Evolução da Arquitetura

Na V5, houve uma evolução da arquitetura, que incluiu a adição dos seguintes elementos:

- Elastick beanstalk

O grupo optou por tornar o processo de deploy da aplicação mais automatizado. Dessa forma, o serviço Elastic Beanstalk implanta e gerencia aplicações e serviços da Web, respeitando o critério de elasticidade. Dentro do Elastic Beanstalk, ele utiliza alguns serviços da AWS. Logo, esses serviços serão usados para a realização deste relatório.
A AWS faz a cobrança do Elastic Beanstalk com base em vários componentes e recursos utilizados no ambiente Elastic Beanstalk, dessa forma, os recursos utilizados para o desenvolvimento da arquitetura foram: 
  
- Route 53 para gerenciamento de domínios.
- CloudFront para melhoria no desempenho e distribuição de conteúdo estático.
- S3 para hospedagem de frontend estático.
- ALB (Balanceador de Carga de Aplicativo) para melhor distribuição de tráfego.
- Bastion Host para acesso seguro às instâncias EC2.
- EC2 t3.medium para instâncias de baixa demanda de CPU.

## Custos Estimados

A tabela abaixo apresenta os custos estimados para cada componente da arquitetura, incluindo os custos em momentos de alto índice de acesso:

|         **Recurso**         | **Custo Mensal (USD)** | **Custo Anual (USD)** |
|:---------------------------:|:-----------------------:|:---------------------:|
|   Instâncias EC2            |   $119.8            |   $1,437.69          |
|   Amazon RDS                |   $32.40  |   $388.8  |
|   Route 53                  |   $1.67  |  $20.04   |
|   CloudFront                |   $50  |   $600  |
|   S3 (Frontend estático)    |   $10   |  $120 |
|   ALB                       |   $20  |   $240  |
|   Bastion Host              |   $22.37  |   $268.44  |

--------------------------------------------------------------------------------------------------------

* Testes de Carga : $8,21 (por evento de alto índice de acesso)  
 * Custo Total em Picos: $24,63 (por dia de alto pico de acesso)

## Vantagens dos Recursos

A arquitetura V5, em relação às arquiteturas anteriores, representa uma grande economia de tempo e recursos. Ao colocar a aplicação em um Elastic Beanstalk, permitiu que o grupo se concentrasse mais na parte dos testes, deixando a parte da arquitetura automatizada.

1. **Route 53**: Gerenciamento escalável de domínios, facilitando o gerenciamento de recursos de rede.

2. **CloudFront**: Melhoria no desempenho e distribuição global de conteúdo estático, oferecendo uma experiência mais rápida aos usuários finais.

3. **S3 (Frontend estático)**: Armazenamento altamente escalável e disponível para recursos estáticos da aplicação.

4. **ALB (Balanceador de Carga de Aplicativo)**: Distribuição equitativa de tráfego para melhorar a disponibilidade e escalabilidade da aplicação.

5. **Bastion Host**: Acesso seguro a instâncias EC2 em uma rede privada, garantindo a segurança da infraestrutura.

6. **EC2 t3.medium**: Opção econômica para instâncias de baixa demanda de CPU, economizando recursos quando necessário.

## Conclusão

A evolução da arquitetura do projeto da V2 para a V5 trouxe melhorias significativas em escalabilidade, desempenho e gerenciamento de recursos.

É importante ressaltar que esta é uma estimativa de custos para um projeto que ainda não foi implantado em produção. Portanto, caso o projeto seja implantado em produção, pode haver diversas alterações nos custos devido ao modelo de precificação da AWS.
