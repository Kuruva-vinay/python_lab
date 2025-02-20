# Implement polymorphism

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

def animal_sound(animal):
    print(animal.speak())

# Create objects of each class
dog = Dog()
cat = Cat()
bird = Bird()

# Call the animal_sound function with different objects
animal_sound(dog)
animal_sound(cat)
animal_sound(bird)
