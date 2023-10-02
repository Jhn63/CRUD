import mysql.connector

class CRUD():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password', #sua senha
            database = 'base',
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    #registrar produto na tabela
    def register(self, cod, name, brand, price):
        query = 'INSERT INTO product (productCod, productName, productBrand, productPrice) VALUES (%s, %s, %s, %s)'
        values = (cod, name, brand, price)
        self.cursor.execute(query, values)
        self.connection.commit()
    
    '''
    def alterar preco do produto

    def pesquisar produto por nome

    def pesquisar produto por marcar

    def remover produto

    def listar produtos por criterio (marcar/preco)

    def exibir dados do produto
    '''

def main(): 
    c = CRUD()
    c.close()

main()