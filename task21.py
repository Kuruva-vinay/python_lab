# Implement inheritance at different levels

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (Single Inheritance)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Derived class (Single Inheritance)
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Derived class (Multilevel Inheritance)
class Puppy(Dog):
    def speak(self):
        return "Yip!"

# Derived class (Hierarchical Inheritance)
class Bulldog(Dog):
    def speak(self):
        return "Woof! Woof!"

# Derived class (Hierarchical Inheritance)
class PersianCat(Cat):
    def speak(self):
        return "Meow! Meow!"

# Create objects of each class and call their speak method
dog = Dog("Buddy")
cat = Cat("Whiskers")
puppy = Puppy("Tiny")
bulldog = Bulldog("Max")
persian_cat = PersianCat("Fluffy")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")
print(f"{puppy.name} says: {puppy.speak()}")
print(f"{bulldog.name} says: {bulldog.speak()}")
print(f"{persian_cat.name} says: {persian_cat.speak()}")
