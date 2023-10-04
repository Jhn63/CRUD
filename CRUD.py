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
        show(result)

    # Pesquisa pela marca
    def searchByBrand(self, brand):
        query = 'SELECT * FROM product WHERE productBrand = %s'
        values = (brand,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        show(result)

    # Pesquisa pelo código (id)
    def searchByCod(self, cod):
        query = 'SELECT * FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        show(result)

    # Remove produto
    def removeProd(self, cod):
        query = 'DELETE FROM product WHERE productCod = %s'
        values = (cod,)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Lista todos os produtos
    def listAllProducts(self):
        query = "SELECT * FROM product"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        show(result)

def show(data):
    print()
    for i in data:
        print(i)

def main():
    c = CRUD()
    while True:
    	print("\n------------ Mercadinho -------------\n")
    	print("1 -  Cadastrar produto")
    	print("2 -  Alterar preço do produto")
    	print("3 -  Pesquisar produto por nome")
    	print("4 -  Pesquisar produto por marca")
    	print("5 -  Pesquisar produto por código")
    	print("6 -  Remover produto")
    	print("7 -  Listar todos os produtos cadastrados")
	
    	print("\n0 -  Sair")
	
    	opcao = input("\nEscolha uma opção: ")
	
    	if opcao == "1":
            try:
                name_register = input('Informe o nome do produto: ')
                cod_register = input('Informe o código do produto: ')
                brand_register = input('Informe a marca do produto: ')
                price_register = input('Informe o preço do produto: ')
                c.register(cod_register, name_register, brand_register, price_register) #Create
            except mysql.connector.IntegrityError as e:
                print("\nO código de registro já existe na base de dados")
            except mysql.connector.errors.DatabaseError as e:
                print("\nErro: valor inserido em campo inválido")
            else:
                print("\nproduto registrado com sucesso")

    	elif opcao == "2":
            cod_alter = input('Informe o código do  produto cujo preço deseja alterar: ')
            newPrice = input('Novo preço: ')
            c.alterPrice(cod_alter, newPrice) #Update
            print("\npreço atualizado com sucesso")

    	elif opcao == "3":
      		name_search = input('Informe o nome do produto que procura: ')
      		c.searchByName(name_search) #Read

    	elif opcao == "4":
      		brand_search = input('Informe a marca do produto que procura: ')
      		c.searchByBrand(brand_search)

    	elif opcao == "5":
      		cod_search = input('Informe o código do produto que procura: ')
      		c.searchByCod(cod_search)

    	elif opcao == "6":
            cod_remove = input('Informe o código do produto que deseja remover: ')
            c.removeProd(cod_remove) #Delete
            print("\nregistro deletado como sucesso")

    	elif opcao == "7":
      		c.listAllProducts()

    	elif opcao == "0":
      		print("Saindo...")
      		break

    	else:
            print("Opção inválida. Tente novamente.")

    c.close()

main()