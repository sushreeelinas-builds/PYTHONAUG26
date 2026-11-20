# The 4 Fundamental Pillars of OOP in Python
# OOP (Object-Oriented Programming) has four important pillars:
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

# 1. Encapsulation
# Definition: Encapsulation means wrapping data (variables) and methods (functions) together inside a class and controlling access to that data.

# In simple words: It protects data from being accessed or modified directly when we want to restrict access.
# Real-life example
# Think about a bank account:
# - Account holder name
# - Account balance
# - Deposit money
# - Withdraw money

# class Bank:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Amount deposited:", amount)

#     def check_balance(self):
#         print("Current balance:", self.__balance)


# b1 = Bank(5000)

# b1.deposit(2000)
# b1.check_balance()

# 2. Inheritance
# Definition: Inheritance means one class can acquire the properties and methods of another class.

# In simple words: A child class can reuse the code of a parent class.

# Types of inheritance:
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical inheritance
# 5. Hybrid inheritance

# class Father:

#     def house(self):
#         print("Father owns a house")

#     def car(self):
#         print("Father owns a car")


# class Son(Father):

#     def bike(self):
#         print("Son owns a bike")


# s1 = Son()

# s1.house()
# s1.car()
# s1.bike()


# a.Single Inheritance (one parent ,one child)
# class vehicle:
#     color = "white"

#     def start(self):
#         print("Vehicle started")

#     def stop(self):
#         print("vehicle stopped")
        
# class bus(vehicle):
    
#     def drive(self):
#         print("Bus is moving ")
        
# b1 = bus()
# b1.start()
# print(b1.color)
    
    
# b. multiple inheritance(multiple parent and one child)

# class Camera:
#     def take_pic(self):
#         print("Taking Photos")
        
# class GPS:
#     def tracking_location(self):
#         print("Location is tracking")
        
# class SmartDevices (Camera,GPS):
#     def connect(self):
#         print ("Devices connected")
            
# sd = SmartDevices()
# sd.take_pic()
# sd.tracking_location()
# sd.connect()


#Multilevel Inheritance in Python
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def driver(self):
#         print("car is moving")


# class ElecticCar(Car):
#     def charge(self):
#         print("Car is charging...")


# e1 = ElecticCar()
# e1.charge()
# c1 =Car()
# c1.charge() // error show because inheritance can not be reverse methord

#Hierarchical Inheritance in Python
# Definition: Hierarchical inheritance is a type of inheritance in which multiple child classes inherit from a single parent class.
# In simple words, One Parent → Multiple Children.

# class Father:

#     def house(self):
#         print("Father owns a house")


# class Son(Father):

#     def bike(self):
#         print("Son owns a bike")


# class Daughter(Father):

#     def car(self):
#         print("Daughter owns a car")


# class Brother(Father):

#     def phone(self):
#         print("Brother has a phone")


# # Creating objects

# s1 = Son()
# d1 = Daughter()
# b1 = Brother()

# s1.house()
# s1.bike()

# d1.house()
# d1.car()

# b1.house()
# b1.phone()


# class Animal:
#     def eat(self):
#         pass

# class Dog(Animal):
#     def legs(self):
#         print("4 legs")

# class Cat(Animal):
#     def sound(self):
#         pass
    
# class Cow(Animal):
#     def sound(self):
#         pass
    
# class Goat(Animal):
#     def sound(self):
#         pass
    
    
    
    
# Hybrid Inheritance in Python
# Definition: Hybrid inheritance is a combination of two or more types of inheritance in a single program.

# In simple words, when we combine inheritance types such as Multiple, Multilevel, 
# and Hierarchical inheritance, it is called Hybrid Inheritance.

# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def driver(self):
#         print("car is moving")


# class bike(Vehicle):
#     def charge(self):
#         print("Bike is riding")
        
# class HybridCar(Car,bike):
#     def  hyfunc(self):
#         print("Hybrid car with both car and bike dunctionality")
    
# h1 = HybridCar()

# h1.start()
# h1.driver()
# h1.charge()
# h1.hyfunc()



#3. Polymorphism ()
# Definition: Polymorphism means one name or method can have different behaviours depending on the object.

# class Cow:
#     def sound(self):
#         print("Cow moo")


# class Cat:
#     def sound(self):
#         print("Cat meows")
        
# class Dog:
#     def sound(self):
#         print("Dog barks")


# d1 = Cow()
# c1 = Cat()

# d1.sound()
# c1.sound()

# 4. Abstraction
# Definition: Abstraction means hiding internal implementation details and showing only essential functionality to the user.
# Python uses the abc module to implement abstraction through abstract classes.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        # Every child class must implement this method
        pass


class Car(Vehicle):
    def start(self):
        # Implementing the require functionlity with common
        print("Car starting...")


class ElectricCar(Vehicle):
    def start(self):
        # Implementing the require functionlity with common
        print("Electric vehicle starting...")


c1 = Car()
c2 = ElectricCar()

c1.start()
c2.start()
