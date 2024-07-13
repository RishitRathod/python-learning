fruit = {"apple":20,"mango":20}
fruit["mango"]=50
print(fruit)
fruit["orange"]=30
print(fruit)

fruit1 = {"a":"c","d":"f"}
fruit.update(fruit1)
print(fruit)
fruit.pop("orange")
print(fruit)