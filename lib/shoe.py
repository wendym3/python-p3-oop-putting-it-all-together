#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand 
        self.size = size 

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        elif value <= 0:
            raise ValueError("Size must be a positive integer")
        else:
            self._size = value
            
    def cobble(self):
        self.condition ="New"
        print("Your shoe is as good as new!")
