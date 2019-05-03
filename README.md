O projeto foi desenvolvido utilizando Docker, de forma facilitiar sua avaliação e instalação de dependências;

Ao rodar o comando docker-compose up --build, é levantado o banco local, com a porta padrão do postgres 5432, usuário: user e senha: 123456;

Para acessar o banco com maior facilidade, foi inserida uma imagem do adminer, disponivel no endereço localhost:8080;

Os jobs fazem acesso a API disponível e criam primordialmente três tabelas no banco warehouse:
tbl_cities -> tabela com informaçṍes de cada cidade, como sua elevação, população, e chave da API;
tbl_hour_city_conditios -> tabela de série temporal com informações de precipitação e temperatura horárias para cada cidade
tbl_daily_city_conditions -> tabela de série temporal com informações de amplitude média por dia para cada cidade

Explicar problemas tidos com a chave de acesso a API;

As queries responsáveis por responser as perguntas estão disponíveis no arquivo queries.sql, dentro da pasta ./views. 
Dentro dessa pasta também está presente um notebook dashboards.ipynb, o qual faz acesso ao banco criado localmente e gera algumas visualizações baseadas nas queries criadas. 
Observa-se que é necessário rodar o jupyter notebook localmente (fora do container docker do projeto) e instalar as dependências necessária na máquina local, caso exista o desejo de gerar dashs atualizados
Existe também uma página html renderizada apenas para visualização, a qual foi criada com dados do dia 05/05/2019

Foi utilizado o sistema de agendamento da biblioteca scheduler do python por fins de simplicidade, pois como não há dependência entre os jobs criados (por garantir que o job inicial é executado sempre que o container é levantado) utilizar o Airflow para agendamento e controle de upstream entre tasks não se mostrou essencial;