class Product:
  def __init__(self,id,name,price,stock):
    self.id=id
    self.name=name
    self.price=price
    self.stock=stock
  def details(self):
    print("Id:",self.id)
    print("Name:",self.name)
    print("Price:",self.price)
    print("Stock:",self.stock)
class User:
  def __init__(self,name,email):
    self.name=name
    self.email=email
    self.cart=ShoppingCart()
  def view_profile(self):
    print("Name:",self.name)
    print("Email:",self.email)

class ShoppingCart:
  def __init__(self):
    self.products={}
   
  def add_product(self,product):
    if product.id in self.products:
      current_quantity=self.products[product.id]["quantity"]
      if current_quantity<product.stock:
          self.products[product.id]["quantity"]+=1
      else:
        print("Out of Stock") 
    
    else:
      if product.stock>0:
        self.products[product.id]={
          "product":product,
          "quantity":1
          }
      else:
        print(f"No stock to add the {product.name}")
  def remove_product(self,product):
    if product.id in self.products:
      if self.products[product.id]["quantity"]==1:
        del self.products[product.id]
      else:
        self.products[product.id]["quantity"]-=1
    else:
      print(f"There is no {product.name} in the cart")
  def calculate_total(self):
    total=0
    for item in self.products.values():
      total+=(item["product"].price)*(item["quantity"])
    return total
  def update_quantity(self,product,quantity):
    if product.id in self.products:
      self.products[product.id]["quantity"]=quantity
    else:
      print(f"No {product.name} to update quantity")
  def empty_cart(self):
    self.products.clear()
  def display_cart(self):
    if self.products:
      print(f'Shopping Cart')
      print(f'{'ID':<5}{'Name':<15}{'Price':<10}{'Qty':<10}{'Total':<10}')
      for item in self.products.values():
        print(f'{item["product"].id:<5}{item["product"].name:<15}{item["product"].price:<10}{item["quantity"]:<10}{item["product"].price*item["quantity"]:<10}')
    else:
      print("Cart is Empty")

if __name__=="__main__":
  # Demo 
  # Create Products
  laptop=Product(1,"Laptop",60000,3)
  phone=Product(2,"Phone",15000,2)
  keyboard=Product(3,"Keyboard",2000,3)

  # Create User
  user=User("Kiran","kiran@gmail.com")

  # Add Products to user cart
  user.cart.add_product(laptop) 
  user.cart.add_product(phone)
  user.cart.add_product(keyboard)

  # Display User Cart
  user.cart.display_cart()

  # Calculate Total Cart Amount
  print(user.cart.calculate_total())

  # Update quantity
  user.cart.update_quantity(phone,5)

  # Display again
  print("\nCart after updating phone quantity:")
  user.cart.display_cart()

  # Remove Product from Cart
  user.cart.remove_product(laptop)
  print("\nCart removing laptop")

  # Display again
  user.cart.display_cart()
  
  # Empty Cart
  user.cart.empty_cart()
  print("\nCart after Empty")

  # Display again
  user.cart.display_cart()

    
  
    
  