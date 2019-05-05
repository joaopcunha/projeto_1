--Query responsável por mostrar as informações da cidade com a maior altitude*
SELECT * FROM tbl_cities WHERE elevation = (SELECT MAX(elevation) from tbl_cities);

--Query responsável por mostrar as informações da cidade com a menor população*
SELECT * FROM tbl_cities WHERE population = (SELECT MIN(population) from tbl_cities);

--Query responsável por mostrar o volume acumulado de precipitações por cidade em um período de tempo
--escolhido dinamicamente. O parametro 36 hour pode ser alterado para determinar a partir de quantas horas
--atrás deseja-se averiguar o volume de precipitação acumulado
SELECT tbl_cities.city_name, grouped_table.sum FROM 
(SELECT city_id, SUM(precipitation) FROM tbl_hour_city_conditions 
WHERE observation_date BETWEEN (NOW() - INTERVAL '36 hour') AND NOW()
GROUP BY city_id) AS grouped_table
JOIN tbl_cities ON tbl_cities.id = grouped_table.city_id;

--Query responsável por montar tabela contendo informações da cidade, e amplitude térmica diária média
--a partir de todos os dados coletados até o momento atual
--Essa query pode responder tanto a pergunta de amplitude térmica média por cidade, quanto sua correlação
--com a altitude das cidades.
SELECT tbl_cities.elevation, tbl_cities.city_name, grouped_table.avg FROM 
(SELECT city_id, AVG(daily_temperature_amplitude) FROM tbl_daily_city_conditions 
GROUP BY city_id) AS grouped_table
JOIN tbl_cities ON tbl_cities.id = grouped_table.city_id;