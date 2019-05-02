O projeto foi desenvolvido utilizando Docker, de forma facilitiar sua avaliação e instalação de dependências;

Ao rodar o comando docker-compose up --build, é levantado o banco local, com a porta padrão do postgres 5432, usuário: user e senha: 123456;

Para acessar o banco com maior facilidade, foi inserida uma imagem do adminer, disponivel no endereço localhost:8080;

Os jobs fazem acesso a API disponível e criam primordialmente três tabelas no banco:
(Explicar sobre as tabelas, e o que elas mostram, com que frequencia são atualizadas);

Explicar problemas tidos com a chave de acesso a API;

As queries responsáveis por responser as perguntas são : XXX (explicar o que cada query mostra, e seus parâmetros). O ideal seria utilizar uma ferramenta de visualização conectando no banco gerado, de forma a montar dashboard com mais facilidade nos seus filtros (série temporal escolhida dinamicamente, e realização de scatterplots para inferir correlações), e visualmente mais apleativos;

Foi utilizado o sistema de agendamento da biblioteca scheduler do python por fins de simplicidade, pois como não há dependência entre os jobs criados (por garantir que o job inicial é executado sempre que o container é levantado) utilizar o Airflow para agendamento e controle de upstream entre tasks não se mostrou essencial;