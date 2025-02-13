class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
print(animal_sound(dog))
print(animal_sound(cat))
