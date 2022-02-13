class Customer:
    name =""
    Lastname = ""
    age = 0

    def addCart(self):
        print("Added to", self.name, self.lastname,"(",self.age,")","'s","cart" )

customer1 = Customer()
customer1.name = "Mann"
customer1.lastname = "L"
customer1.age = "30"

customer2 = Customer()
customer2.name = "Eve"
customer2.lastname = "B"
customer2.age = "20"

customer3 = Customer()
customer3.name = "AA"
customer3.lastname = "B"
customer3.age = "29"

customer1.addCart()
customer2.addCart()
customer3.addCart()
