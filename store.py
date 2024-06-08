import mysql.connector

class StoreManager():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'senha', #sua senha
            database = 'store',
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    # registrar produto
    def register_product(self, name, categ, brand, descript, stored, price):
        query = """
            INSERT INTO produto (nome_produto, categoria, marca, descricao, qtd_estoque, preco) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, categ, brand, descript, stored, price)
        self.cursor.execute(query, values)
        self.connection.commit()

    # registrar cliente
    def register_client(self, name, phone_number, email, addres):
        query = """
            INSERT INTO cliente (nome_cliente, telefone, email, endereco) 
            VALUES (%s, %s, %s, %s)
        """
        values = (name, phone_number, email, addres)
        self.cursor.execute(query, values)
        self.connection.commit()

    # etapa 1 da compra (setup) 
    def temp_item_table(self):
        query = 'CALL tabela_item_temp()'
        self.cursor.execute(query)
        self.connection.commit()

    # etapa 2 to n-1 da compra (adicionando ao carrinho)
    def add_to_cart(self, product_id, quantity):
        query = """
            INSERT INTO temp_item (id_produto, quantidade, valor)
            SELECT id_produto, %s, preco * %s
            FROM produto
            WHERE id_produto = %s;
        """
        values = (quantity, quantity, product_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    # etapa n (efetuando compra)
    def finish_purchase(self, client_id, date, payment_method, state):
        query = 'CALL efetuar_compra(%s,%s,%s,%s)'
        values = (client_id, date, payment_method, state)
        self.cursor.execute(query, values)
        self.connection.commit()
    