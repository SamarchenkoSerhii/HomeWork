class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, {self.description}, {self.dimensions}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.numberphone}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt 
        else:
            self.products[item] = cnt

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())

    def __str__(self):
        items_str = "\n".join([f"{item.name}: {count} pcs." for item, count in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}\nTotal: {self.get_total()}"


lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")
print(lemon) 

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer) 

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User), "Екземпляр класу User"
assert cart.get_total() == 60, "Всього 60"

cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 80, "Повинно залишатися 80!"
