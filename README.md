<b>SOBRE O PROJETO</b>

O código aqui apresentado tem como objetivo manter os dois jobs rodando diariamente para atualizar as informações de um banco de dados. Isso foi realizado a partir de consultas a uma API de dados metereológicos e do mecanismo de agendamento da biblioteca scheduler do Python.

Descrição das pastas:
1) ./api: contém a classe de comunicação com a API da AccuWeather. <br>
2) ./dbcoon: contém a classe de comunicação com o banco de dados utilizado (postgresql).<br>
3) ./infra: contém as variáveis de ambiente utilizadas no projeto, como as credenciais do banco e o token de acesso à API.<br>
4) ./jobs: contém o código dos processos de ETL responsáveis por realizar as requisições e atualizar o banco de dados.<br>
5) ./scripts: contém um script inicial para criação e população do banco, o qual é executado ao subir o projeto.<br>
6) ./views: contém as queries que podem ser realizadas para responder as informações de interesse; um notebook ipynb como algumas visualizações realizadas com dados do dia 04/05/2019; e uma relatório estático em html estático deste notebook.

<b>INSTALANDO E RODANDO</b>

O projeto foi desenvolvido utilizando Docker de forma a facilitiar sua avaliação, configuração e instalação de dependências;

Ao rodar o comando docker-compose up --build, as dependência são instaladas, as variáveis de ambientes configurdas e são leventados 3 containers.<br>
-> Um banco de dados local em postgresql, com a porta 5433, usuário: user, senha: 123456 e nome do banco: warehouse;<br>
-> Uma imagem do adminer, disponível na porta 8080 de modo a facilitar as consultas ao banco;<br>
-> O container do projeto que roda o script inicial e o processo de agendamento dos jobs diários;

Os jobs atualizam primordialmente três tabelas no banco warehouse:<br>
*tbl_cities* -> tabela com informaçṍes de cada cidade, como sua elevação, população, e chave da API;<br>
*tbl_hour_city_conditios* -> tabela de série temporal com informações de precipitação e temperatura horárias para cada cidade;<br>
*tbl_daily_city_conditions* -> tabela de série temporal com informações de amplitude média por dia para cada cidade;

As cidades presentes no banco são:
São Paulo, Santos, Ribeirão Preto, Sorocaba, São José dos Campos, Atibaia, Bauru, Presidente Prudente, Campinas e Campos do Jordão.

Observação: caso exista a necessidade de gerar dashs atualizados é preciso rodar o jupyter notebook localmente e instalar as dependências necessárias na máquina local, visto que não foi gerada uma imagem do jupyter notebook.
