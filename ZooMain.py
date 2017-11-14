from Animals import Animal, Fish, Dino, Bird, Snake

def animals():
#     a = Animal("Larry", "Lobster", "Red")
#     print(a)
#     
#     b = Fish("Nemo", "Clownfish", "Orange", "3", "2")
#     print(b)
#     
#     c = Dino("Tina", "Raptor", "Blue", True, 3)
#     print(c)
#     
#     d = Bird("Theodore", "Cardinal", "Red", 47, 12)
#     print(d)
#     
#     e = Snake("Guido van Rossum", "Human", "Pasty", False, "Tallish")
#     print(e)
#     
#     print("Animals: {0}".format(b.animal_count()))
#     print("Fish: {0}".format(b.fish_count()))
#     print("Dinos: {0}".format(c.dino_count()))
#     print("Birds: {0}".format(d.bird_count()))
#     print("Snakes: {0}".format(e.snake_count()))
    
#     a = Animal("CJ", "Gorilla", "Grey")
#     a2 = Animal("CJ", "Gorilla", "Grey")
#     b = Animal("Copernicus", "Armadillo", "Brown")
#     
#     c = Fish("Nemo", "Clownfish", "Orange", 3.5, 2)
#     c2 = Fish("Nemo", "Clownfish", "Orange", 3.5, 2)
#     
#     d = Fish("Bruce", "Shark", "Grey", 4, 2)
    
#     print("Equiv: {0}".format(c == c))
#     print("NE: {0}".format(c != d))
#     print("LT: {0}".format(c < d))
#     print("LE: {0}".format(c <= d))
#     print("GT: {0}".format(c > d))
#     print("GE: {0}".format(c >= c2))

#     print("Equiv: {0}".format(c == '!'))
#     print("NEq: {0}".format(c != '!'))
#     print("LT: {0}".format(b <= 1))
#     print("LE: {0}".format(c <= b))
#     print("GT: {0}".format(c > b))
#     print("GE: {0}".format(c >= b))
    
    
    fishL = []
    for i in range(300):
        fishL.append(Fish())
  
    for f in fishL:
        print(f)
        
    fishL.sort()
    
    print("\n")
    
    for f in fishL:
        print(f)

if __name__ == '__main__':
    animals()