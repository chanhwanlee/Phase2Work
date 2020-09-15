class Person:
  def __init__(self, name:str, height:int, strength:int, health_points:int):
    self.name = name
    self.height = height
    self.strength = strength
    self.health_points = 100

  def __str__(self) -> str:
    return f"{self.name} {self.health_points}"
  
  def introduce(self) -> str:
    return f"Hello, my name is {self.name}"
  
  def punch(self, object) -> None:
    object.health_points -= 10

  def eat(self) -> None:
    self.health_points = 100
  
peter = Person("Peter Lee", 173, 9000, 100)
nick = Person("Nicolas Palmar", 140, 1, 100)

print (peter)
print (nick)

print (peter.introduce())
print (nick.introduce())

print (nick.health_points)
peter.punch(nick)
print (nick.health_points)

print (peter.health_points)
peter.punch(peter)
print (peter.health_points)

peter.eat()
print (peter.health_points)
