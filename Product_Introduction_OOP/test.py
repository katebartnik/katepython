from Product_Class import Product
from Shop_Class import Shop

waterProductObject = Product(1, "Water", 2.99)
breadProductObject = Product(2, "Bread", 3.99)
breadProductObject.setQuantity(20)

ourShopObject = Shop()
ourShopObject.appendProduct(waterProductObject)
ourShopObject.appendProduct(breadProductObject)
ourShopObjectProducts = ourShopObject.getProductList()


for product in ourShopObjectProducts:
    print(product.getName())
    print(product.getPrice())
    print(product.getQuantity())
    print(product.getUrlPictures())


findedProduct = ourShopObject.resolveProductById(1)
print(findedProduct.getName())

# ourShopObject.appendProduct()
