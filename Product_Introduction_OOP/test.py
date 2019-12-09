from Product_Class import Product
from Shop_Class import Shop

waterProductObject = Product(1, "Water", 2.99)
breadProductObject = Product(2, "Bread", 3.99)
chipsProductObject = Product(3, "Chips", 5.99)
carrotProductObject = Product(6, "Carrot", 1.99)


ourShopObject = Shop()
ourShopObject.appendProduct(waterProductObject)
ourShopObject.appendProduct(breadProductObject)
ourShopObject.appendProduct(chipsProductObject)
ourShopObject.printProductList()


ourShopObject.removeProductById(2)
ourShopObject.appendProduct(carrotProductObject)
ourShopObject.printProductList()