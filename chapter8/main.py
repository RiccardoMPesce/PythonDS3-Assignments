class Item:
    def __init__(self):
        pass 
    
    def set_price(self, price : float, inplace=False):
        self._price = price
        if inplace: return self

    def get_price(self):
        return self._price
    
    def delete_price(self):
        self._price = -1
    
    price : float = property(get_price, set_price, delete_price)
    
    def __repr__(self):
        return f"Item(Price: {self._price})"
    def __str__(self):
        return f"Item(Price: {self._price})"

def main():
    print(Item().set_price(0.95))
    i = Item()

    i.price = 0.95
    del i.price

    print(i.price)

if __name__ == "__main__":
    main()