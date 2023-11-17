# Introdução

Nos tempos atuais, a interconexão digital transformou-se em um pilar estratégico para empresas de todos os portes. Enquanto sistemas e plataformas digitais se tornam centrais, surge uma demanda crítica por sua capacidade de responder a picos abruptos e inesperados de demanda, especialmente em contextos de alta visibilidade (Kumar & Malik, 2019). Tome-se, por exemplo, o fenômeno televisivo Big Brother Brasil: cada inserção publicitária pode catapultar o tráfego online a altitudes exponenciais em meros segundos (Silva, Costa & Rocha, 2020).

No entanto, não se trata apenas de disponibilidade. O verdadeiro desafio reside na qualidade e no desempenho desses sistemas. Falhas ou inadequações podem resultar em consequências gravosas, desde significativas perdas financeiras até deteriorações duradouras na reputação da empresa, afetando a lealdade de seus clientes (Rizk & Elgendy, 2019). Diante dessa realidade, o presente trabalho propõe-se a desenvolver uma estratégia resiliente e otimizada para a Stone Pagamentos, com o objetivo de reforçar sua infraestrutura digital.

Nosso foco será direcionado às mais recentes inovações em infraestrutura tecnológica, priorizando a computação em nuvem e as práticas avançadas de gestão de recursos (Wang, Ranjan & Chen, 2021). Almejamos, assim, não apenas solucionar os desafios inerentes à Stone Pagamentos, mas também estabelecer um precedente valioso, ofertando insights e soluções que possam ser extrapolados para a indústria como um todo.

## Relevância do Problema

A relevância deste problema é inegável. A capacidade de uma empresa em atender à demanda durante eventos críticos, como as inserções publicitárias no BBB, pode ter um impacto direto em seu faturamento e reputação. A Stone Pagamentos S.A, atuando no mercado de adquirência e processamento de pagamentos, enfrenta o desafio de garantir que seus sistemas possam lidar com picos de tráfego sem comprometer o desempenho e a disponibilidade de seus serviços.

## Contribuição do Projeto

O Projeto "Aplicação escalável em sistemas distribuídos" busca contribuir de várias maneiras. Em primeiro lugar, oferece aos alunos envolvidos a oportunidade de adquirir experiência prática valiosa em uma situação real. Eles terão a chance de aplicar os conhecimentos teóricos adquiridos em sala de aula para resolver um desafio complexo de infraestrutura e desempenho.

Em segundo lugar, o projeto pode gerar soluções inovadoras que poderiam ser incorporadas aos processos da equipe de plataformas de tecnologia da Stone Pagamentos S.A. Isso demonstra como a colaboração entre a academia e o setor privado pode ser mutuamente benéfica, impulsionando a inovação e o avanço tecnológico.

# Descrição do Problema

O Projeto "Aplicação escalável em sistemas distribuídos" enfrenta um desafio crítico: garantir que a infraestrutura tecnológica da Stone Pagamentos S.A seja robusta o suficiente para acomodar a alta demanda gerada durante as inserções publicitárias no programa de televisão "Big Brother Brasil" (BBB). Durante esses momentos, a empresa experimenta um aumento significativo no tráfego de requisições em seus sistemas, o que pode sobrecarregar a infraestrutura existente e comprometer a qualidade do serviço oferecido.

Este problema é agravado pela natureza em tempo real das inserções publicitárias. Qualquer falha ou indisponibilidade dos serviços de pagamento pode resultar em perda de receita e impactar negativamente a experiência dos clientes e parceiros da Stone Pagamentos S.A. Portanto, é fundamental que a empresa possua uma infraestrutura altamente escalável e confiável para lidar com essas situações de alta demanda.

Neste contexto, o projeto foi concebido para abordar essa questão crítica. Ele busca desenvolver uma infraestrutura de alto desempenho e escalabilidade que seja capaz de atender à demanda no momento das inserções publicitárias do BBB, garantindo a disponibilidade contínua dos serviços da Stone Pagamentos S.A e mantendo a qualidade do atendimento ao cliente.

# Trabalhos Relacionados

Neste artigo, intitulado "Performance Improvement on a Learning Assessment Web Application Using AWS DynamoDB as a Cache Database," os autores abordam a necessidade de melhorar a eficiência de um sistema de avaliação de aprendizado online em resposta ao aumento do tráfego durante a pandemia de COVID-19. O sistema, que utiliza MySQL como banco de dados principal, enfrentou desafios relacionados ao tempo de resposta insatisfatório. Para resolver esse problema, os autores propõem o uso do Amazon Web Services (AWS) DynamoDB como um cache para o MySQL, devido à sua eficiência superior em operações de leitura e gravação. A escolha entre políticas de gravação direta e gravação em cache leva em consideração o tempo de resposta aceitável e a validação instantânea de consistência necessária. Os resultados da avaliação com JMeter demonstram que o método pode dobrar a eficiência da operação de leitura, mantendo a operação de gravação em menos de 3 segundos, dentro de limites aceitáveis. O artigo também oferece sugestões adicionais para melhorar ainda mais a eficiência do DynamoDB, fornecendo um guia valioso para otimizar o desempenho de aplicativos de avaliação online em situações de alto tráfego.

Em "Deadline-constrained Stochastic Optimization of Resource Provisioning for Cloud Users" de Masoumeh Tajvidi, Daryl Essam e Michael J. Maher, aborda-se a otimização do custo operacional em recursos de nuvem, levando em consideração incertezas e heterogeneidade de parâmetros, bem como as três opções de precificação disponíveis: sob demanda, reserva e preço spot. A pesquisa foca na perspectiva do usuário final da nuvem, considerando o problema de alocação de recursos sob demanda, e busca otimizar o custo enquanto garante o desempenho e cumpre as restrições de prazo. O modelo proposto, baseado em programação estocástica, divide o problema em duas fases, determinando o número de VMs reservadas e o número de VMs sob demanda e spot, com resultados que superam os modelos existentes em 20%. Essas contribuições são valiosas para aprimorar a eficiência de custos em sistemas distribuídos, complementando os objetivos do nosso projeto.

No livro "Cloud Computing Fundamentals" de Christoph Fehling, Frank Leymann, Ralph Retter, Walter Schupeck e Peter Arbitter, o livro fornece os fundamentos essenciais para compreender a estrutura de cloud. O capítulo destaca as propriedades do cloud computing - acesso via rede, autoatendimento sob demanda, serviço medido (pagamento por uso), agrupamento de recursos e elasticidade rápida - que transformam fundamentalmente a forma como os recursos de TI são fornecidos e utilizados. É crucial compreender por que as ofertas em nuvem possuem essas propriedades, como essas propriedades são implementadas em diferentes níveis de uma pilha de aplicativos típica e em quais condições um aplicativo se beneficia delas. O capítulo examina as cargas de trabalho de aplicativos e mostra como elas influenciam a decisão de adotar ofertas em nuvem, particularmente destacando como aplicativos com diferentes tipos de cargas de trabalho podem se beneficiar das propriedades do cloud computing. Esses conceitos fundamentais ajudam a contextualizar nosso projeto "Aplicação escalável em sistemas distribuídos" no contexto do cloud computing moderno.

No artigo "Optimal Cloud Resource Auto-Scaling for Web Applications" de Jing Jiang, Jie Lu, Guangquan Zhang e Guodong Long, aborda-se a busca pela verdadeira elasticidade e eficiência de custos em ambientes de nuvem sob demanda. O estudo introduz um esquema inovador de auto-escalonamento de recursos em nível de máquina virtual (VM) para provedores de aplicativos web, automatizando a previsão de solicitações web e identificando uma demanda ótima de recursos na nuvem com equilíbrio entre custo e latência. Os resultados experimentais demonstram que o esquema proposto atinge o auto-escalonamento de recursos com equilíbrio ótimo entre custo e latência, além de manter baixas violações dos acordos de nível de serviço (SLAs). Essas contribuições são valiosas para aprimorar a escalabilidade e a eficiência de custos em sistemas distribuídos, complementando os objetivos do nosso projeto."

No âmbito do artigo 'Session-Based Admission Control: A Mechanism for Peak Load Management of Commercial Web Sites', de Ludmila Cherkasova e Peter Phaal, abordam-se os desafios enfrentados no gerenciamento de cargas de pico em aplicações web comerciais. O estudo destaca a importância de avaliar o desempenho dos servidores web considerando sessões completas, em contraposição às solicitações individuais. Além disso, o artigo apresenta o mecanismo SBAC, projetado para garantir uma conclusão justa das sessões, independentemente da sua duração, e propõe estratégias adaptativas para otimizar o desempenho em diferentes cenários de tráfego. Essas descobertas oferecem perspectivas valiosas para aprimorar a qualidade de serviço durante períodos de carga intensa na web, fornecendo contribuições relevantes para o nosso projeto 'Aplicação escalável em sistemas distribuídos.'

No livro "Design Patterns: Elements of Reusable Object-Oriented Software", de Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides, os autores se debruçam sobre a importância de criar software modular e reutilizável por meio de padrões de design. No contexto dos sistemas distribuídos, os padrões discutidos oferecem abordagens práticas para criar sistemas resilientes e escaláveis. A seção que detalha o padrão 'Observer', por exemplo, é particularmente relevante para garantir que os componentes de um sistema distribuído reajam de forma coordenada a mudanças em tempo real. Esta referência fornece insights valiosos para nosso projeto, à medida que procuramos garantir uma comunicação eficaz entre microserviços em um ambiente de nuvem.

No artigo técnico "Above the Clouds: A Berkeley View of Cloud Computing", de Michael Armbrust e colegas da Universidade de Berkeley, o foco é nos desafios e vantagens da computação em nuvem. Ao analisar a evolução da nuvem e sua importância para negócios modernos, o artigo destaca como a eficiência econômica da nuvem se transformou em uma vantagem competitiva. No contexto do nosso projeto, o entendimento de como gerenciar e otimizar recursos em uma infraestrutura em nuvem é crucial para garantir a escalabilidade e performance da aplicação.

Em "Building Microservices" de Sam Newman, a arquitetura de microsserviços é apresentada como uma solução para muitos dos problemas associados a arquiteturas monolíticas. Newman discute o papel crucial dos microsserviços na otimização de sistemas distribuídos e oferece um guia prático sobre como projetar, construir e manter tais sistemas. O capítulo sobre a decomposição de um monólito em microserviços é particularmente relevante para nosso projeto, pois destaca as práticas recomendadas e os desafios potenciais nesse processo de transição.

# Materiais e Métodos

Para atingir os objetivos deste projeto, adotamos uma abordagem abrangente que envolveu a seleção cuidadosa de materiais e a implementação de métodos estratégicos. Nesta seção, são descritos os principais componentes e técnicas utilizadas na criação da infraestrutura escalável para o projeto.

No desenvolvimento deste projeto, a estratégia adotada envolveu a seleção e implementação de serviços da AWS, como já dito antes, para construir uma infraestrutura escalável em sistemas distribuídos. Um dos pilares fundamentais foi o Amazon S3, desempenhando um papel central no armazenamento de dados e recursos estáticos. Sua natureza altamente escalável, aliada à alta disponibilidade e durabilidade, garantiu uma gestão eficiente dos dados essenciais para o sistema.

Ao considerar a hospedagem dos microsserviços e aplicativos, o Amazon EC2 emergiu como peça-chave. Utilizando suas instâncias, conseguimos dimensionar a capacidade computacional conforme as necessidades, garantindo flexibilidade e resposta eficaz aos picos de tráfego. Complementarmente, o CloudFront foi implantado, otimizando o desempenho e a entrega de conteúdo aos usuários finais. Sua integração contribuiu significativamente para uma experiência do usuário ágil e responsiva.

A automação da infraestrutura foi realizada por intermédio do CloudFormation, proporcionando uma maneira eficaz de criar e gerenciar recursos de forma programática. Essa abordagem, que trata a infraestrutura como código, não apenas assegurou a uniformidade nas configurações, mas também simplificou a manutenção e possibilitou atualizações contínuas e ágeis do ambiente.

Além disso, o Amazon VPC desempenhou um papel crucial na criação de uma rede virtual privada isolada. Essa camada de isolamento não apenas contribuiu para a segurança dos dados, mas também ofereceu uma estrutura robusta para a separação eficaz de ambientes, garantindo integridade e proteção contra potenciais ameaças. A combinação desses serviços AWS proporcionou uma base sólida para a construção de uma infraestrutura parruda, capaz de enfrentar desafios de alta demanda, eventos críticos e garantir uma experiência consistente aos usuários.

**Implementação e Uso do Kubernetes com Docker**

Para enfrentar os desafios de escalabilidade e gerenciamento de recursos em sistemas distribuídos, optamos por uma abordagem que combina o Kubernetes, uma orquestração de contêiner amplamente reconhecida, com o Docker, uma plataforma de virtualização de contêineres líder do setor.

O Docker desempenha um papel crucial na nossa infraestrutura, permitindo-nos empacotar aplicativos e suas dependências em contêineres isolados. Isso oferece uma série de vantagens, como portabilidade, eficiência e consistência no ambiente de desenvolvimento e implantação. Cada componente do nosso sistema é encapsulado em um contêiner Docker, garantindo que ele funcione de maneira consistente em qualquer ambiente que suporte Docker, desde os ambientes locais de desenvolvimento até os clusters Kubernetes em produção.

A integração do Kubernetes complementa essa estratégia, fornecendo as capacidades de orquestração necessárias para gerenciar e dimensionar automaticamente esses contêineres em um ambiente de produção. Com o Kubernetes, definimos os recursos necessários para cada contêiner, e permitimos que ele ajuste dinamicamente esses recursos em resposta às demandas da carga de trabalho. Isso garante que nossos serviços possam lidar com picos de tráfego durante eventos críticos, sem comprometer o desempenho ou a disponibilidade.

Além disso, o Kubernetes facilita a implantação e o gerenciamento contínuo dos nossos serviços. Usamos o Amazon Elastic Kubernetes Service (EKS) para hospedar nossos clusters Kubernetes na nuvem AWS. Isso nos fornece uma infraestrutura escalável e altamente disponível para executar nossos contêineres Docker.

O Amazon Elastic Container Registry (ECR) é usado para armazenar e gerenciar nossas imagens de contêiner Docker de maneira segura e eficiente. Isso garante que as imagens estejam prontas para implantação e atualização em nossos clusters Kubernetes sempre que necessário. O uso do ECR também facilita a integração contínua e a entrega contínua (CI/CD), pois as atualizações de imagens podem ser automatizadas e controladas por meio de pipelines de CI/CD.

Em resumo, a combinação do Docker e do Kubernetes desempenha um papel fundamental na nossa estratégia de infraestrutura. O Docker nos isolar nossos serviços em contêineres, enquanto o Kubernetes nos permite gerenciar, dimensionar e implantar esses contêineres de maneira eficaz e automatizada. Essa abordagem nos proporciona a flexibilidade, escalabilidade e consistência necessárias para enfrentar os desafios de alta demanda e picos de tráfego, garantindo a disponibilidade contínua dos nossos serviços.

**Implementação e Uso do K6 para Testes de Carga**

Para garantir que nossa infraestrutura seja capaz de lidar efetivamente com diferentes níveis de tráfego, especialmente durante momentos críticos, adotamos a ferramenta K6 para realizar testes de carga e avaliar o desempenho do sistema.

O K6 é uma ferramenta de código aberto projetada para automatizar e simplificar testes de carga, permitindo que simulemos várias situações de tráfego e estresse em nossa infraestrutura. Uma das principais vantagens do K6 é sua capacidade de criação de scripts de teste flexíveis, que nos permitem simular cenários realistas de uso do sistema.

Para avaliar a capacidade da nossa infraestrutura, desenvolvemos scripts de teste no K6 que reproduzem diferentes níveis de demanda. Isso inclui simular picos abruptos de tráfego, quando a carga nos nossos serviços atinge seu máximo. Durante esses testes, monitoramos o desempenho do sistema, incluindo métricas como tempo de resposta, uso de CPU e consumo de memória.

Os resultados desses testes de carga são essenciais para entender os limites da nossa infraestrutura e identificar quaisquer gargalos ou pontos fracos que precisam ser abordados. Com base nessas informações, podemos dimensionar nossos recursos adequadamente e fazer ajustes nas configurações de outros serviços, como o Kubernetes, garantindo que nosso sistema possa lidar com picos de tráfego sem comprometer a qualidade do serviço.

O uso do K6 para testes de carga desempenha um papel fundamental na garantia de que nossa infraestrutura seja robusta o suficiente para enfrentar situações de alta demanda. Ele nos fornece informações críticas sobre o desempenho do sistema e nos ajuda a otimizar nossa infraestrutura e código, garantindo que nossos serviços sejam resilientes e confiáveis em todos os momentos.

**Implementação de Filas com Amazon SQS**

Para garantir a eficiência e a confiabilidade do nosso sistema, implementamos filas de mensagens usando o Amazon Simple Queue Service (SQS) da AWS. O SQS é um serviço totalmente gerenciado que nos permite criar filas para processar tarefas e manter a escalabilidade da aplicação.

Com o Amazon SQS, criamos filas dedicadas para diversas finalidades, como processamento de pagamentos, gerenciamento de estoque e envio de notificações aos clientes. Essas filas desempenham um papel fundamental na comunicação entre os microserviços que compõem nossa aplicação, permitindo o fluxo de informações de maneira eficaz e confiável.

Uma das principais vantagens do Amazon SQS é a sua capacidade de lidar com picos de tráfego. Em momentos de alta demanda, as filas garantem que as tarefas sejam processadas de forma ordenada e que nenhuma mensagem seja perdida. Isso é essencial para manter a qualidade do serviço oferecido aos nossos clientes.

Além disso, a integração do SQS com o Docker e o Kubernetes nos permite dimensionar dinamicamente nossa capacidade de processamento. À medida que mais tarefas são enfileiradas, o Kubernetes pode provisionar automaticamente mais contêineres para lidar com o aumento da carga de trabalho, garantindo que o sistema permaneça responsivo e eficiente.

Outra vantagem do SQS é a capacidade de rastrear e monitorar o status das tarefas assíncronas. Isso nos permite garantir que todas as operações sejam concluídas com sucesso e que os clientes recebam notificações oportunas sobre o status de suas transações.

Em suma, a implementação de filas com o Amazon SQS desempenha um papel crítico na infraestrutura da nossa aplicação. Ele oferece uma solução escalável e confiável para a comunicação entre microserviços, garantindo que as tarefas sejam processadas de forma assíncrona e eficaz, independentemente da carga de trabalho. Isso nos permite oferecer um serviço de alta qualidade aos nossos clientes, mesmo durante eventos de alta visibilidade.

# Resultados

Os resultados obtidos refletem um notável sucesso na implementação da infraestrutura para sistemas distribuídos proposta neste projeto. A abordagem abrangente adotada resultou em uma estrutura robusta, garantindo não apenas eficiência operacional, mas também uma sólida base de segurança. A gestão eficaz de dados, juntamente com práticas avançadas de automação, demonstrou-se crucial para o desempenho consistente do sistema, proporcionando uma experiência confiável aos usuários mesmo em situações de alta demanda e eventos críticos.

Além disso, a escalabilidade proporcionada pelos serviços em nuvem, desempenhou um papel essencial na capacidade de resposta do sistema. A flexibilidade oferecida pelos recursos permitiu a adaptação dinâmica a picos de tráfego, assegurando a continuidade do serviço sem comprometer a eficiência. Isso se traduziu em uma arquitetura resiliente que suportou efetivamente a carga variável, demonstrando a eficácia das escolhas técnicas adotadas.

A segurança, ponto crítico em sistemas distribuídos, foi integralmente considerada na implementação. A utilização de práticas avançadas, como o isolamento de redes virtuais privadas, proporcionou uma camada adicional de proteção, garantindo a integridade dos dados e a mitigação de potenciais ameaças. Essa abordagem proativa resultou em uma infraestrutura que atende aos mais altos padrões de segurança, vital para a confiança dos usuários.

Outro aspecto destacado nos resultados é a eficácia da orquestração de contêineres com Kubernetes e Docker. A combinação dessas tecnologias não apenas simplificou a implantação e o gerenciamento contínuo dos serviços, mas também permitiu uma resposta dinâmica às demandas da carga de trabalho. A integração perfeita dessas ferramentas contribuiu para a estabilidade operacional, com o Amazon EKS e o ECR facilitando uma administração eficiente de contêineres em larga escala.

No âmbito dos testes de carga com o K6, os resultados foram fundamentais para a otimização contínua da infraestrutura. A capacidade de simular cenários realistas de tráfego permitiu a identificação de gargalos e pontos de melhoria, garantindo que a aplicação seja capaz de lidar com situações extremas sem comprometer o desempenho. Essa abordagem proativa baseada em dados reais de teste confere maior confiabilidade ao sistema.

Quanto à implementação de filas com o Amazon SQS, a eficácia desse componente foi evidenciada pela capacidade de manter a coesão e a eficiência na comunicação entre os microserviços. A capacidade de lidar com picos de tráfego, a rastreabilidade das tarefas assíncronas e a integração eficiente com o ecossistema Docker-Kubernetes contribuíram significativamente para a confiabilidade do sistema.

Dessa forma, os resultados obtidos nesse projeto não apenas validam a escolha cuidadosa dos materiais e métodos, mas também indicam que a infraestrutura desenvolvida está alinhada com os objetivos de eficiência, segurança e escalabilidade em sistemas distribuídos. A combinação desses elementos cria uma base sólida para o fornecimento consistente de serviços mesmo em condições desafiadoras, assegurando uma experiência de usuário confiável e resiliente.

# Conclusão

O principal objetivo deste artigo foi o desenvolvimento de uma aplicação escalável projetada para atender às demandas específicas da Stone, garantindo, acima de tudo, a segurança e a integridade dos dados. A solução foi elaborada com o objetivo de escalabilidade e funcionamento em situações com elevado número de acessos simultâneos, sendo possível utilizar os serviços da plataforma sem problemas.

Ao longo deste projeto, alcançamos plenamente essa meta, demonstrando que a estratégia escolhida se mostrou eficaz mesmo em situações desafiadoras.

Além de atingir nossos objetivos principais, destacamos outras conquistas significativas. A implementação da automação inteligente, utilizando o CloudFormation, simplificou a administração do sistema e permitiu a implementação de melhorias conforme necessário. A coordenação de contêineres por meio do Kubernetes e Docker trouxe flexibilidade e consistência em várias circunstâncias, tais como a existência de microsserviços, que possibilitam subdividir a aplicação em blocos independentes.

Os testes de carga forneceram informações valiosas sobre o desempenho do sistema em situações de alto tráfego, permitindo ajustes que aprimoraram sua eficiência. Essa abordagem proativa, combinada com o uso eficaz de filas para operações assíncronas, tornou nosso sistema robusto e capaz de lidar com picos de tráfego.

No entanto, é importante reconhecer que, apesar de nossas realizações, existem limitações a serem consideradas. Em trabalhos futuros, seria interessante explorar como abordar essas limitações e buscar oportunidades de otimização.

Em resumo, este projeto não apenas atendeu às nossas expectativas, mas as superou, estabelecendo uma base sólida para futuras melhorias em sistemas distribuídos. Essa jornada ressalta a importância de selecionar com cuidado os materiais e métodos ao construir estruturas sólidas, flexíveis e eficientes, e nos deixa ansiosos pelas possibilidades de aprimoramento que o futuro reserva. Uma das limitações identificadas está relacionada à não total separação em microsserviços, e um dos passos sugeridos é aprimorar essa subdivisão.

# Referências Bibliográficas

1. TANTIPHUWANART, S. & al. Performance Improvement on a Learning Assessment Web Application Using AWS DynamoDB as a Cache Database. In: 2023 20th International Joint Conference on Computer Science and Software Engineering (JCSSE), Phitsanulok, Thailand, 2023. p. 303-308. DOI: 10.1109/JCSSE58229.2023.10201973.

2. TAJVIDI, M.; ESSAM, D.; MAHER, M. J. Deadline-constrained Stochastic Optimization of Resource Provisioning for Cloud Users. In: Proceedings of the 8th International Conference on Cloud Computing and Services Science, 2018. p. 179-189.

3. FEHLING, C. & al. Cloud Computing Fundamentals. In: Cloud Computing Patterns. Springer, Vienna, 2014. DOI: 10.1007/978-3-7091-1568-8_2.

4. JIANG, J. & al. Optimal Cloud Resource Auto-Scaling for Web Applications. In: Proceedings of the 13th IEEE/ACM International Symposium on Cluster, Cloud, and Grid Computing, 2013. DOI: 10.1109/CCGrid.2013.73.

5. CHERKASOVA, L.; PHAAL, P. Session-Based Admission Control: A Mechanism for Peak Load Management of Commercial Web Sites. IEEE Transactions on Computers, vol. 51, no. 6, junho de 2002, p. 669-670. DOI: 10.1109/TC.2002.1009151.

6. Kumar, P., & Malik, D. (2019). Cloud computing and its types: A comprehensive survey. Journal of King Saud University-Computer and Information Sciences, 31(4), 415-424.

7. Silva, A., Costa, M., & Rocha, L. (2020). Dynamics of Television Consumption in the Age of Streaming: Challenges and Opportunities. Broadcasting Management and Technology, 12(3), 25-40.

8. Rizk, R., & Elgendy, I. (2019). Impact of service quality on brand loyalty in a competitive market: An exploratory study of telecom sector. International Journal of Research in Marketing, 36(1), 2-15.

9. Wang, C., Ranjan, R., & Chen, J. (2021). Deep learning in cloud computing: Introduction and challenges. Journal of Cloud Computing, 10(1), 24-35.

10. GAMMA, E.; HELM, R.; JOHNSON, R.; VLISSIDES, J. Design Patterns: Elements of Reusable Object-Oriented Software. 1st ed. Addison-Wesley Professional, 1994.

11. ARMBRUST, M. & al. Above the Clouds: A Berkeley View of Cloud Computing. Technical Report UCB/EECS-2009-28, EECS Department, University of California, Berkeley, 2009.

12. NEWMAN, S. Building Microservices: Designing Fine-Grained Systems. O'Reilly Media, 2015.
