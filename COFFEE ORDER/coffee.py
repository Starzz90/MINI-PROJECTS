import csv


class Order:
    def __init__(self, customer, name, price, addon, discount):
        self.customer = customer
        self.name = name
        self.price = price  # kept as a list to match total_price()/CSV layout
        self.addon = addon
        self.discount = discount

    def total_price(self):
        return sum(self.price)


class Reportorder:
    def __init__(self, filename="ORDER.csv"):
        self.order = []
        self.filename = filename
        self.loadFile()

    def loadFile(self):
        self.order.clear()
        try:
            with open(self.filename, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    customer = row[0]
                    discount = 0.0

                    if len(row) >= 5:
                        # customer, name, price..., addon, discount
                        name = row[1]
                        try:
                            price = [int(value) for value in row[2:-2]]
                        except ValueError:
                            price = []
                        addon = row[-2].strip() if row[-2].strip() else "No add-on"
                        try:
                            discount = float(row[-1])
                        except ValueError:
                            discount = 0.0
                    elif len(row) == 4:
                        # customer, name, price, addon (no discount saved)
                        name = row[1]
                        try:
                            price = [int(row[2])]
                        except ValueError:
                            price = []
                        addon = row[3].strip() if row[3].strip() else "No add-on"
                    elif len(row) == 3:
                        name = row[1]
                        try:
                            price = [int(row[2])]
                            addon = "No add-on"
                        except ValueError:
                            price = []
                            addon = row[2].strip() if row[2].strip() else "No add-on"
                    elif len(row) == 2:
                        name = row[1]
                        price = []
                        addon = "No add-on"
                    else:
                        continue

                    self.order.append(Order(customer, name, price, addon, discount))
        except FileNotFoundError:
            print("File", self.filename, "not found. Create new file!!!")

    def saveFile(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for order in self.order:
                writer.writerow(
                    [order.customer, order.name] + order.price + [order.addon, order.discount]
                )

    def Add_order(self, order):
        self.order.append(order)
        self.saveFile()

    def orderList(self):
        if not self.order:
            print("No orders yet!")
            return
        print("DAFTAR ORDER:")
        for i, order in enumerate(self.order):
            print(
                f"{i}. Customer: {order.customer} | {order.name} - Price: {order.total_price()} "
                f"- Add-on: {order.addon} - Discount: {order.discount}"
            )
        print()

    def total_earnings(self):
        return sum(order.total_price() for order in self.order)

    def order_count(self):
        return len(self.order)

    def Deleteorder(self, index):
        del self.order[index]
        self.saveFile()

    def DeleteorderAll(self):
        self.order.clear()
        self.saveFile()


COFFEE_MENU = {
    "1": ("Espresso", 15000),
    "2": ("Latte", 20000),
    "3": ("Cappuccino", 25000),
    "4": ("Americano", 18000),
}

ADDON_MENU = {
    "1": ("Extra Shot", 3000),
    "2": ("Soy Milk", 5000),
    "3": ("Vanilla Syrup", 2000),
    "4": ("Caramel Syrup", 2000),
    "5": ("No add-on", 0),
}


def add_order_flow(manager):
    customer = input("Input customer name: ")

    print(
        "Available coffee: \n 1. Espresso (15000)\n 2. Latte (20000)"
        "\n 3. Cappuccino (25000)\n 4. Americano (18000)"
    )
    ordered = input("Input order Name: ")
    if ordered not in COFFEE_MENU:
        print("Coffee is not available; please choose a valid option.")
        return
    name, price = COFFEE_MENU[ordered]

    print(
        "Available add-on: \n 1. Extra Shot (+3000)\n 2. Soy Milk (+5000)"
        "\n 3. Vanilla Syrup (+2000)\n 4. Caramel Syrup (+2000) \n 5. No add-on"
    )
    addonchoice = input("Input add-on number: ")
    if addonchoice not in ADDON_MENU:
        print("Add-on is not available; using No add-on")
        addon, addon_price = "No add-on", 0
    else:
        addon, addon_price = ADDON_MENU[addonchoice]
    price += addon_price

    discount_rate = 0.0
    while True:
        discount = input("Is customer a member? (yes/no): ")
        if discount.lower() == "yes":
            print("Member discount applied: 10% off")
            discount_rate = 0.1
            break
        elif discount.lower() == "no":
            print("No discount applied")
            discount_rate = 0.0
            break
        else:
            print("Please answer yes or no.")

    final_price = int(price * (1 - discount_rate))
    manager.Add_order(Order(customer, name, [final_price], addon, discount_rate))
    print("Order added")
    print(
        f"Customer: {customer}, Order: {name}, Price: {final_price}, "
        f"Add-on: {addon}, Discount: {discount_rate}"
    )


def Main():
    manager = Reportorder()

    while True:
        start_shift = input("Start Shift? (yes/no): ")
        if start_shift.lower() == "no":
            print("Thank you for using this program")
            break
        elif start_shift.lower() != "yes":
            print("Please answer yes or no.")
            continue

        employee = input("Input employee name: ")

        while True:
            print("Please insert the following choices:")
            print(
                " 1.   Show order \n 2.   Add order    \n 3.   Delete order  "
                "\n 4.   Delete previous shift orders  \n 5.   Exit Choices and Shift"
            )
            choice = input("Choice: ")

            if choice == "1":
                manager.orderList()
            elif choice == "2":
                add_order_flow(manager)
            elif choice == "3":
                manager.orderList()
                try:
                    index = int(input("Enter the number of the order you want to delete= "))
                    if 0 <= index < len(manager.order):
                        manager.Deleteorder(index)
                        print("Order deleted")
                    else:
                        print("Order not found")
                except ValueError:
                    print("Order not found")
            elif choice == "4":
                manager.orderList()
                confirm = input("Are you sure you want to delete all orders? (yes/no): ")
                if confirm.lower() == "yes":
                    manager.DeleteorderAll()
                    print("All orders deleted")
                else:
                    print("Operation cancelled")
            elif choice == "5":
                count = manager.order_count()
                total = manager.total_earnings()
                print("End Shift Summary")
                print("Employee Name:", employee)
                print(f"Total orders: {count}")
                print(f"Total earnings: {total}")
                print("Thank you for using this program")
                break
            else:
                print("Please choose a valid option from the menu.")
            # loop continues automatically until choice == "5" breaks it above


if __name__ == "__main__":
    Main()