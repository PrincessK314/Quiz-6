from dataclasses import dataclass

@dataclass
class Item():
    name: str
    quantity: int
    price: float

class Cart():
    def __init__(self):
        self.cart = []
    
    def addItem(self, name: str, inv: list[Item]) -> None:
        i = [item for item in self.cart if item.name == name]
        if len(i) != 0:
            i[0].quantity += 1
        else:
            j = [item for item in inv if item.name == name]
            if len(j) != 0:
                self.cart.append(Item(name, 1, j[0].price))
            else:
                print("No " + name + " in stock")


@dataclass
class OrderInfo():
    custName: str
    custID: int
    address: str
    email: str
    cart: Cart

class CalculatePrice():
    def __init__(self, tax: float, discount: float):
        self.tax = tax
        self.discount = discount

    def calculateTotalPrice(self, cart: Cart) -> float:
        sum = 0
        for i in cart.cart:
            sum += i.quantity * i.price
        sum *= (1 - self.discount)
        sum += self.tax * sum
        return sum
    
class ConfirmInfo():
    def checkAvailability(self, inv: list[Item], cart: Cart) -> None:
        for i in cart.cart:
            j = [item for item in inv if item.name == i.name]
            if len(j) != 0:
                if i.quantity > j[0].quantity:
                    print("More " + i.name + " in cart than available. Quanity is being lowered to " + str(j[0].quantity))
                    if (j[0].quantity == 0):
                        cart.cart.remove(i)
                    else:
                        i.quantity = j[0].quantity
            else:
                print("No " + i.name + " are in stock. Removing from cart")
                cart.cart.remove(i)

    def confirmUserInfo(self, info: OrderInfo) -> None:
        print("Verify your information\n")
        print("Name: " + info.custName)
        print("Address: " + info.address)
        print("Email: " + info.email)
        response = input("\nIs this correct (y/n): ")
        if response == "n" or response == "N":
            info.custName = input("Enter your name: ")
            info.address = input("Enter your address: ")
            info.email = input("Enter your email: ")

class EmailConfirmation():
    def sendConfirmationEmail(self, info: OrderInfo) -> None:
        print("Confirmation Email Sent to " + info.email)

class UpdateInv():
    def update(self, inv: list[Item], cart: Cart) -> None:
        for item in cart.cart:
            j = [i for i in inv if i.name == item.name]
            j[0].quantity -= item.quantity
        cart.cart.clear()

class Order():
    def __init__(self, name: str, id: int, address: str, email: str, tax: float, discount: float):
        self.info = OrderInfo(name, id, address, email, Cart())
        self.priceCalculator = CalculatePrice(tax, discount)
        self.confirm = ConfirmInfo()
        self.email = EmailConfirmation()
        self.update = UpdateInv()

    def addItem(self, name: str, inv: list[Item]):
        self.info.cart.addItem(name, inv)
    
    def checkout(self, inv: list[Item]):
        self.confirm.checkAvailability(inv, self.info.cart)
        price = self.priceCalculator.calculateTotalPrice(self.info.cart)
        print("\nTotal Price: " + "{:.2f}".format(price))
        self.confirm.confirmUserInfo(self.info)
        self.email.sendConfirmationEmail(self.info)
        self.update.update(inv, self.info.cart)

def main():
    shopInverntory = [Item("milk", 5, 4.99), Item("bread", 2, 3.99), Item("eggs", 8, 9.99), Item("ham", 4, 7.99)]

    order = Order("Bob", 1234, "123 Generic Road", "abd123@gmail.com", 0.05, 0.02)
    order.addItem("milk", shopInverntory)
    order.addItem("bread", shopInverntory)
    order.addItem("cheese", shopInverntory)
    order.addItem("bread", shopInverntory)
    order.addItem("milk", shopInverntory)
    order.addItem("bread", shopInverntory)
    order.addItem("ham", shopInverntory)
    order.addItem("ham", shopInverntory)

    order.checkout(shopInverntory)

main()
