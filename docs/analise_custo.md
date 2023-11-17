# Análise de Gestão de Custo

## Introdução

Neste relatório, apresentamos uma análise financeira atualizada do projeto "Aplicação escalável em sistemas distribuídos". A análise considera a evolução da arquitetura da versão 1 (V1) para a versão 2 (V2) e inclui informações críticas sobre custos em momentos de alto índice de acesso. O objetivo é fornecer uma visão abrangente dos custos envolvidos na execução do projeto e avaliar as vantagens de cada componente da arquitetura.

## Evolução da Arquitetura

Na V1 do projeto, a arquitetura proposta incluía instâncias EC2 (C5.18xlarge, r5.16xlarge, P3.2xlarge) e Amazon RDS. As vantagens desses recursos incluíam alta capacidade de processamento, gerenciamento simplificado de banco de dados e capacidade de aceleração por GPU.

Na V2, houve uma evolução da arquitetura, que incluiu a adição dos seguintes elementos:

- Route 53 para gerenciamento de domínios.
- CloudFront para melhoria no desempenho e distribuição de conteúdo estático.
- S3 para hospedagem de frontend estático.
- ALB (Balanceador de Carga de Aplicativo) para melhor distribuição de tráfego.
- Bastion Host para acesso seguro às instâncias EC2.
- EC2 t3.medium para instâncias de baixa demanda de CPU.

Essa evolução da arquitetura trouxe uma expansão significativa da infraestrutura do projeto, com foco em escalabilidade e desempenho.

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

A arquitetura da V1 inicialmente proposta incluía instâncias EC2 com alta capacidade de processamento e Amazon RDS com gerenciamento simplificado de banco de dados. Esses recursos foram escolhidos por suas vantagens específicas, incluindo o equilíbrio entre CPU e memória, capacidade de aceleração por GPU e escalabilidade eficiente. Entretanto eram recursos muito caros e fora da realidade para nosso projeto.

A evolução para a V2 trouxe uma ampla gama de vantagens adicionais, além de se ajustar a realidade do aws lab:

1. **Route 53**: Gerenciamento escalável de domínios, facilitando o gerenciamento de recursos de rede.

2. **CloudFront**: Melhoria no desempenho e distribuição global de conteúdo estático, oferecendo uma experiência mais rápida aos usuários finais.

3. **S3 (Frontend estático)**: Armazenamento altamente escalável e disponível para recursos estáticos da aplicação.

4. **ALB (Balanceador de Carga de Aplicativo)**: Distribuição equitativa de tráfego para melhorar a disponibilidade e escalabilidade da aplicação.

5. **Bastion Host**: Acesso seguro a instâncias EC2 em uma rede privada, garantindo a segurança da infraestrutura.

6. **EC2 t3.medium**: Opção econômica para instâncias de baixa demanda de CPU, economizando recursos quando necessário.

## Conclusão

A evolução da arquitetura do projeto da V1 para a V2 trouxe melhorias significativas em escalabilidade, desempenho e gerenciamento de recursos. A combinação dos recursos da V1 com os recursos da V2 cria uma infraestrutura robusta e escalável.

Importante ressaltar que essa é uma estimativa de custos de um projeto que não foi para produção. Portanto, caso o projeto seja implantado em produção podem haver diversas alterações nesses custos, por conta do modelo de precificação da AWS. 
