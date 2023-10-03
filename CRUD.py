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

    # registrar produto na tabela
    def register(self, cod, name, brand, price):
        query = 'INSERT INTO product (productCod, productName, productBrand, productPrice) VALUES (%s, %s, %s, %s)'
        values = (cod, name, brand, price)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Altera o preço
    def alterPrice(self, cod, newPrice):
        query = 'UPDATE product SET productPrice = %s WHERE productCod = %s'
        values = (newPrice, cod)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Pesquisa pelo nome
    def searchByName(self, name):
        query = 'SELECT * FROM product WHERE productName = %s'
        values = (name,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    # Pesquisa pela marca
    def searchByBrand(self, brand):
        query = 'SELECT * FROM product WHERE productBrand = %s'
        values = (brand,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    # Pesquisa pelo código (id)
    def searchByCod(self, cod):
        query = 'SELECT * FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    # Remove produto
    def removeProd(self, cod):
        query = 'DELETE FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Exibe os dados do produto
    def showProdData(self, cod):
        query = 'SELECT * FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result

    # Lista todos os produtos
    def listAllProducts(self):
        query = "SELECT * FROM product"
        self.cursor.execute(query)
        return self.cursor.fetchall()

<<<<<<< HEAD
    
=======

def main():
    c = CRUD()

    result = c.listAllProducts()
    print(result)
>>>>>>> 36ac005257cbf666fe895701fcd8e3cea7734005

    c = CRUD()
    c.close()
    
main()