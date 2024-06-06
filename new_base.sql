CREATE DATABASE IF NOT EXISTS store;
USE store;

CREATE TABLE cliente (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(20) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
	email VARCHAR(30) UNIQUE NOT NULL,
    endereco VARCHAR(50) NOT NULL
);

CREATE TABLE produto (
	id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(20) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
	marca VARCHAR(20) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    qtd_estoque INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE compra (
	id_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_compra DATE NOT NULL,
    forma_pagamento VARCHAR(20) NOT NULL,
    situacao VARCHAR(20) NOT NULL,
    montante DECIMAL(10,2) NOT NULL,
    
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE item (
	id_compra INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    
    PRIMARY KEY (id_compra, id_produto),
    CONSTRAINT fk_compra FOREIGN KEY (id_compra) REFERENCES compra (id_compra),
    CONSTRAINT fk_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

INSERT INTO produto(nome_produto, categoria, marca, descricao, qtd_estoque, preco) VALUES
('Camiseta Básica', 'Vestuário', 'Marca A', 'Camiseta de algodão 100%', 100, 29.99),
('Calça Jeans', 'Vestuário', 'Marca B', 'Calça jeans slim fit', 50, 99.99),
('Jaqueta de Couro', 'Vestuário', 'Marca B', 'Jaqueta de couro sintético', 25, 199.99),
('Tênis Esportivo', 'Vestuário', 'Marca D', 'Tênis para corrida', 75, 149.99),
('Vestido Floral', 'Vestuário', 'Marca E', 'Vestido com estampa floral', 30, 79.99);

INSERT INTO cliente (nome_cliente, telefone, email, endereco) VALUES 
('Ana Silva', '123-456-7890', 'ana.silva@example.com', 'Rua A, 123, Cidade X'),
('João Souza', '987-654-3210', 'joao.souza@example.com', 'Avenida B, 456, Cidade Y'),
('Maria Oliveira', '555-123-4567', 'maria.oliveira@example.com', 'Praça C, 789, Cidade Z'),
('Carlos Pereira', '444-987-6543', 'carlos.pereira@example.com', 'Rua D, 321, Cidade W'),
('Luciana Alves', '333-555-1234', 'luciana.alves@example.com', 'Avenida E, 654, Cidade V');

DELIMITER //
CREATE PROCEDURE store.tabela_item_temp()
BEGIN
	CREATE TEMPORARY TABLE IF NOT EXISTS temp_item(
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);
DELETE FROM temp_item;
END //
DELIMITER ;

-- procedure para efetuar uma compra
DELIMITER //
CREATE PROCEDURE store.efetuar_compra(
    IN id_cli INT,
    IN data_comp DATE,
    IN forma_pag VARCHAR(50),
    IN situacao VARCHAR(50)
) BEGIN
	-- registrando compra
	INSERT INTO store.compra (id_cliente, data_compra, forma_pagamento, situacao, montante) VALUES
	(id_cli, data_comp, forma_pag, situacao, (SELECT SUM(valor) AS total FROM temp_item));
    
    -- adicionando itens da compra a tabela verdadeira
    INSERT INTO store.item (id_compra, id_produto, quantidade, valor) 
	SELECT 
		(SELECT id_compra FROM store.compra ORDER BY id_compra DESC LIMIT 1) AS id_compra,
		id_produto, 
		quantidade, 
		valor 
	FROM temp_item;

	-- atualizando estoque
	UPDATE store.produto AS p
	JOIN temp_item AS t ON p.id_produto = t.id_produto
	SET p.qtd_estoque = p.qtd_estoque - t.quantidade;
END //
DELIMITER ;