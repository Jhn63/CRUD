from store import StoreManager

def main():
	c = StoreManager()
	c.temp_item_table()
	c.add_to_cart(2,3)
	c.add_to_cart(5,1)
	c.finish_purchase(3,'2024-06-06','pix','pago')
	c.close()

main()