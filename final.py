class Pet:
  none = 0
  speciesList = ['dog', 'cat', 'horse', 'hamster']

  def __init__(self, species = none, name =""):
    if species.lower() not in self.speciesList:
      raise Exception
    self.species = species
    self.name = name

  def __str__(self):
    returnValue = "Species of:" + self.species + "named"
    if len(name) > 0:
      returnValue = returnValue + self.name
    else:
      returnValue = returnValue + "unnamed"
    return returnValue

class Dog(Pet):
  def __init__(self, name = "", chases = "Cats"):
    Pet.__init__(self, "Dog", name)
    self.chases = chases

  def __str__(self):
    returnValue = "Species of Dog =, Named"
    if len(name) > 0:
      returnValue = returnValue + self.name
    else:
      returnValue = returnValue + "unnamed"

    returnValue = returnValue + "Chases" + self.chases
    return returnValue

class Cat(Pet):
  def __init__(self, name = "", hates = "Dogs"):
    Pet.__init__(self, "Cat", name)
    self.hates = hates

  def __str__(self):
    returnValue = "Species of Cat =, Named"
    if len(name) > 0:
      returnValue = returnValue + self.name
    else:
      returnValue = returnValue + "unnamed"

    returnValue = returnValue + "Hates" + self.hates
    return returnValue

def main():
  dict = {
    "Dog": [],
    "Cat": []
  }
  for i in range(5):
    dict["Dog"].append(Dog("Dog " + i))
  for i in range(3):
    dict["Cat"].append(Cat("Cat " + i))

