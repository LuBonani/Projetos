USE sucos_vendas;

SELECT * FROM tabela_de_clientes;

SELECT CPF AS IDENTIFICADOR, NOME AS CLIENTE FROM tabela_de_clientes;


SELECT * FROM tabela_de_produtos;

SELECT * FROM tabela_de_produtos WHERE CODIGO_DO_PRODUTO = '1000889';

SELECT * FROM tabela_de_produtos WHERE SABOR='MANGA';

SELECT * FROM tabela_de_produtos WHERE NOME_DO_PRODUTO BETWEEN 'f' AND 'FZ';