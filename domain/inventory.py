#   Local BD

product_details = {
  "Pants" : {
    "id_product" : 'pants01',
    "product_name" : 'blue pants',
    "price" : 32.000,
    "quantity" : 30
  },
  "Shoes" : {
    "id_product" : 'shoes01',
    "product_name" : 'brown shoes',
    "price" : 23.000,
    "quantity" : 50
  },
  "Hats" : {
    "id_product" : 'hat01',
    "product_name" : 'black hat',
    "price" : 15.000,
    "quantity" : 300
  }
}

# Basic menu

def show_menu():
  print ("""
  1. Show categories
  2. Show products details
  3. Add new product
  4. Search product by id
  5. Exit""")

# Main method

def run():
  print('\n*** Basic local inventory ***')
  show_menu()
  option = int(input('\nPlease enter an option: '))

  def option_case(option):
    match option:
      case 1: show_categories()
      case 2: show_details_products()
      case 3: add_product(input('Enter product name: '))
      case 4: find_product_by_id(input('Enter product id: '))
      case 5: exit_option()
  option_case(option)

# Deploy categories

def show_categories():
  for product in product_details:
    print(product)

# Deploy product details

def show_details_products():
  for product in product_details.items():
    print(product)

# Method for adding product

def add_product(product_name):
  product_details [product_name]= {
    "id_product": input("Product ID: "),
    "product_name": input("Product name: "),
    "price": input("Product price: "),
    "quantity": input("Product quantity: ")
  }

# Find product by id

def find_product_by_id(id_product):
  string_id = str(id_product)
  for product in product_details.values():
    if product['id_product'] == string_id:
      print(product)

# Exit

def exit_option():
  print('See you later')
  exit()

# TODO: Execution Code

while True:
  run()