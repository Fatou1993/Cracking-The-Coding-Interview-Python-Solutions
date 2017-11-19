from collections import deque

class AnimalShelter(object):
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = deque()

    def enqueue(self, a):
        if a.type == "dog":
            self.dogs.append(a)
            self.order.append(1)
        else:
            self.cats.append(a)
            self.order.append(0)

    def dequeueDog(self):
        if self.dogs:
            return self.dogs.popleft()
        return None

    def dequeueCat(self):
        if self.cats:
            return self.cats.popleft()
        return None

    def dequeueAny(self):
        if self.order:
            firstEntered = self.order.popleft()
            if firstEntered : #dogs
                return self.dogs.popleft()
            else:
                return self.cats.popleft()
        return None



class Animal(object):
    def __init__(self, type):
        self.type = type

class Dog(Animal):
    def __init__(self, name="Dexter"):
        Animal.__init__(self, "dog")
        self.name = name

    def __str__(self):
        return "I am a dog and my name is "+ self.name

class Cat(Animal):
    def __init__(self, name="Minou"):
        Animal.__init__(self, "cat")
        self.name = name

    def __str__(self):
        return "I am a cat and my name is "+ self.name


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue(Dog("Bella"))
    shelter.enqueue(Cat("Ashes"))
    shelter.enqueue(Dog("Lucy"))
    shelter.enqueue(Dog("Daisy"))
    shelter.enqueue(Cat("Tiger"))
    shelter.enqueue(Cat("Misty"))
    shelter.enqueue(Dog("Oscar"))
    shelter.enqueue(Dog())
    x = shelter.dequeueAny()
    print(x, isinstance(x, Dog))
    print(shelter.dequeueAny())
