import mysql.connector

class CRUD():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '@Me130626', #sua senha
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
    
    def alterPrice(self, cod, newPrice):
        query = 'UPDATE product SET productPrice = %s WHERE productCod = %s'
        values = (newPrice, cod)
        self.cursor.execute(query, values)
        self.connection.commit()

    def searchByName(self, name):
        query = 'SELECT * FROM product WHERE productName = %s'
        values = (name,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def searchByBrand(self, brand):
        query = 'SELECT * FROM product WHERE productBrand = %s'
        values = (brand,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def searchByCod(self, cod):
        query = 'SELECT * FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    '''
    def remover produto

    def exibir dados do produto

    '''

def main(): 
    c = CRUD()
    
    result = c.searchByName("leite")
    print(result)

    c.close()

main()