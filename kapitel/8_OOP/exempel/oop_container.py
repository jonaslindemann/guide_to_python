# -*- coding: utf-8 -*-

class Container:
    def __init__(self):
        self.__items = []

    def __len__(self):
        print("(__len__) Returnerar längden av containern")
        return len(self.__items)
    
    def __getitem__(self, index):
        print(f"(__getitem__) Hämtar värdet vid index {index}")
        return self.__items[index]
    
    def __setitem__(self, index, value):
        print(f"(__setitem__) Sätter värdet vid {index} to {value}")
        self.__items[index] = value

    def __contains__(self, item):
        print(f"(__contains__)Undersöker om {item} finns i containern")
        return item in self.__items
    
    def append(self, item):
        print(f"Lägger till: {item}")
        self.__items.append(item)

    def __str__(self):
        return "Container with items: " + str(self.__items)
    
# Exempel på användning:
if __name__ == "__main__":
    c = Container()
    c.append(10)
    c.append(20)
    c.append(30)
    
    print(f"Längd på containern: {len(c)}")
    
    print(f"Element vid index 1: {c[1]}")
    
    c[1] = 25
    print(f"Efter uppdatering, element vid index 1: {c[1]}")
    
    print(f"Finns 20 i containern? {'Yes' if 20 in c else 'No'}")
    print(f"Finns 25 i containern? {'Yes' if 25 in c else 'No'}")
    
    print(c)    