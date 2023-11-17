# Grupo 5  
<table>
<td><a href= "https://www.inteli.edu.br/"><img src="./docs/img/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Introdução

Este é o repositório dos arquivos dos alunos do Módulo 7 do curso de Ciência da Computação do Inteli no 3º trimestre de 2023. Durante este trimestre está sendo desenvolvido um projeto em parceria com a Stone.

# Projeto: *Aplicação escalável em sistemas distribuídos*

# Grupo: *Stonks*

# Integrantes:

* [Beny Frid](mailto:Beny.Frid@sou.inteli.edu.br)
* [Cristiane De Andrade Coutinho](mailto:Cristiane.Coutinho@sou.inteli.edu.br)
* [Felipe Sampaio](mailto:Felipe.Silva@sou.inteli.edu.br)
* [Luiz Carlos da Silva Júnior](mailto:Luiz.Junior@sou.inteli.edu.br)
* [Rafael Cabral](mailto:Rafael.Cabral@sou.inteli.edu.br)
* [Stefano Butori](mailto:Stefano.Butori@sou.inteli.edu.br)
* [Thomas Brand](mailto:Thomas.Brand@sou.inteli.edu.br)

# Descrição

**Sistema capaz de Lidar com Cargas Intensas para Aplicações Essenciais**

**Problema:**
Este projeto aborda um problema comum enfrentado por muitas aplicações web robustas. Durante momentos críticos, como os intervalos comerciais do programa *Big Brother Brasil* (BBB), a aplicação precisa enfrentar um aumento significativo no número de acessos simultâneos. Esses picos de tráfego repentinos podem sobrecarregar a aplicação, levando a atrasos, lentidão e até falhas no sistema. Garantir que a aplicação mantenha um desempenho ótimo mesmo sob essas condições extremas é um desafio fundamental.

**Projeto:**
O foco deste projeto é projetar e implementar uma solução que permita que a aplicação supere com sucesso os momentos de alta demanda. A abordagem envolve a criação de uma arquitetura escalável usando a tecnologia de cluster Kubernetes em um ambiente de nuvem (AWS). Isso permitirá que a aplicação se adapte automaticamente ao aumento repentino de acessos, distribuindo eficientemente a carga entre os componentes. Além disso, será desenvolvido um sistema de testes com o uso do k6 para simular esses picos de tráfego e avaliar a capacidade de resposta da aplicação. 


## Documentação

Os arquivos da documentação deste projeto estão na pasta [docs/index.md](docs/index.md), e o seu conteúdo é publicado via GitHub Pages.



## Artigo do Projeto

O artigo detalhado do projeto pode ser encontrado no caminho docs/artigo.md.

## Configurações para desenvolvimento

Este projeto foi desenvolvido usando Flask para o backend e uma combinação de HTML, CSS e JavaScript para a interface de usuário. Para configurar seu ambiente de desenvolvimento e contribuir para o projeto, siga estes passos:

## Instalação do Python

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo do [site oficial do Python](https://www.python.org/downloads/).

## Instalação do Flask

Flask é um micro-framework para Python usado para desenvolver aplicações web. Instale o Flask usando o seguinte comando no terminal:

```
pip install Flask
```

## Clonagem do Repositório

Faça o clone do repositório do projeto para sua máquina local. Isso pode ser feito através do comando git:

```
git clone [URL do repositório]
```

Substitua `[URL do repositório]` pelo link do repositório do projeto.

## Configuração do Docker

Para cofigurar o projeto em uma Docker na EC2 da AWS você deve fazer o download no [link](https://github.com/2023M7T1-Inteli/Grupo-4/blob/main/codigo_mvp_basico/sprint_4_codigo_mvp/backend/aplication/Dockerfile) dentro de sua EC2.

No terminal da EC2 rode os seguintes comandos:

1- sudo service docker start

2 - docker ps -a
(Obs: Se no status aparecer "UP" está funcionando, se estiver funcionando você acessa essa rota: "http://44.202.5.66/", para fazer os testes. Caso contrário, rode os comandos abaixo)

3- docker rm "ID do container"
(obs: O ID do container vai aparecer quando rodar o comando anterior, você só precisa digitar somente os primeiros 4 elementos/algarismos)

4 - sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000

5 - sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT

6 - Docker run --name teste -p 8000:8000 luizpsj20/stonks-backend

7 - Repita o passo 2

## Executando o Projeto

Após clonar o repositório e instalar as dependências necessárias, navegue até a pasta do projeto e execute o arquivo principal em Python. Este arquivo contém o código para iniciar o servidor Flask e servir a aplicação web.

```
python [nome do arquivo].py
```

Substitua `[nome do arquivo]` pelo nome do arquivo Python que inicia o servidor Flask.

## Navegação e Testes

Com o servidor Flask rodando, você poderá acessar a aplicação web através do navegador, geralmente no endereço `http://localhost:5000`. Explore as funcionalidades da aplicação e faça modificações conforme necessário.

## Desenvolvimento e Contribuição

Faça alterações no código, teste as modificações e contribua com melhorias. Certifique-se de seguir as diretrizes de contribuição do projeto.

## Configurações para desenvolvimento

Para executar o projeto, é necessário executar o arquivo em Python dentro da Sprint_5, lá está a versão final do projeto com todo ambiente de execução


## Tags Gerais:

**SPRINT 1:**
- Desenvolvimento do protótipo inicial e aplicação com arquitetura básica.
Análise do negócio.
- Definição dos Requisitos Funcionais e Não Funcionais.
- Pesquisa sobre o público-alvo.

**SPRINT 2:**
- Estruturação da arquitetura corporativa.
- Desenvolvimento do Front-end.
- Implementação do Back-end.
- Primeira versão do Artigo.

**SPRINT 3:**
- Modelagem e Implementação detalhada.
- Nova versão do Artigo.
- Aprimoramento da interface

**SPRINT 4:**
- Realização de testes no sistema.
- Elaboração do Relatório Técnico.
- Definição e refinamento da aplicação.
- Terceira versão do Artigo.

**SPRINT 5:**
- Aperfeiçoamentos finais na aplicação.
- Finalização e submissão do Artigo completo.
- Finalização dos testes.
- Análise de Gestão de Custo do projeto.

## Licenças:

<table>
  <tr><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"></tr>
</table>
<table>
  <tr><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></tr>
</table>
[Application 4.0 International](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1)
