# **Question 1 – Book Details**
# Create a `Book` class with:
# - Book name
# - Author name
# - Price
# Use a constructor to initialize the values and a method to display book details.

# class Book:
    
#     def __init__(self,name,author,price):
#         self.name=name
#         self.author=author
#         self.price=price
        
#     def BookDetails(self):
#         print("Book name :", self.name)
#         print("Author :", self.author)
#         print("Book Price :", self.price)
        
# book1 = Book("Rich Dad Poor Dad","Robert Kiyosaki",359)
# book1.BookDetails()



# **Question 2 – Rectangle**
# Create a `Rectangle` class with length and width.
# Create two methods:
# - `area()` – Calculate area.
# - `perimeter()` – Calculate perimeter.

# class Rectangle:
    
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2*(self.length + self.width)
    
# Rec1=Rectangle(20,10)

# print("Area :", Rec1.area())
# print("Periment :", Rec1.perimeter())




# **Question 3 – Movie Ticket**
# Create a `MovieTicket` class with movie name and ticket price.
# Create methods to:
# - Display movie details.
# - Calculate total price for multiple tickets.

# class movie:
    
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
        
#     def Display(self):
#         print("Movie name :",self.name)
#         print("Ticket Price :",self.price)
        
#     def Ticket(self, num_ofTicket):
#         total_price = self.price * num_ofTicket
#         print("Number of Tickets :",num_ofTicket)
#         print("Total Price :",total_price)

# movie1 = movie("Conjuring" , 200)

# movie1.Display()
# movie1.Ticket(4)  
        
        
# **Question 4 – Electricity Bill**
# Create an `ElectricityBill` class with customer name and units consumed.
# Calculate the bill using ₹5 per unit.

# class Electricity:
    
#     def __init__(self,name):
#         self.name = name
        
#     def Display(self):
#         print("Customer name :",self.name)
        
#     def bill(self,units):
#         per_unit = 5
#         total_consumed =units * per_unit
#         print("Units consumed :",units)
#         print("Total :",total_consumed,"units consumed")
        
# Ele1 = Electricity("Rahul")

# Ele1.Display()
# Ele1.bill(22)




# **Question 5 – Shopping Cart**
# Create a `ShoppingCart` class with product name, price, and quantity.
# Create methods to:
# - Display product details.
# - Calculate total price.
# - Apply a 10% discount if the total price is above ₹5,000.

class Shopping:
    
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def Display(self):
        print("Product name :", self.name)
        print("Product price :", self.price)
        print("Product quantity :", self.quantity)
        
    def Pricedetails(self):
        Total_price = self.price * self.quantity
        
        if Total_price > 5000:
            Discount = (Total_price * 10)/100
            Discount_price = Total_price - Discount
            print("Total price :",Total_price)
            print("10% Discount Price :",Discount_price)
            
        else:
            print("No Discount Available")
            print("Total price :",Total_price)
            
shop1 = Shopping("Dress",2000,4)

shop1.Display()
shop1.Pricedetails()
        
    
        
