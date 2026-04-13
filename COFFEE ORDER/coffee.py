import csv

class menu:
    # nama dan price
    def __init__(self, customer, coffee, price, addon):
        self.coffee = coffee
        self.price = price
        self.addon = addon
        self.customer = customer

class Order:
    def __init__(self, customer, name, price, addon):
        self.name = name
        self.price = price
        self.addon = addon
        self.customer = customer


    def total_price(self):
        return sum(self.price)

class Reportorder:
    def __init__(self, filename = "ORDER.csv"):
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
                    if len(row) >= 4:
                        name = row[1]
                        price = []
                        try:
                            price = [int(value) for value in row[2:-1]]
                        except ValueError:
                            price = []
                        addon = row[-1].strip() if row[-1].strip() else "No add-on"
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
                    self.order.append(Order(customer, name, price, addon))
        except FileNotFoundError:
            print("File", self.filename, "not found. Create new file!!!")
    
    def saveFile(self):
        with open(self.filename, "w", newline= "") as file:
            writer = csv.writer(file)
            for order in self.order:
                writer.writerow([order.customer] + [order.name] + order.price + [order.addon])
        
    # def add order
    def Add_order(self, order):
        self.order.append(order)
        # simpan data
        self.saveFile()
        
    def orderList(self):
        if not self.order:
            print("Tidak ada data")
            return
        print("DAFTAR ORDER:")
        for i, order in enumerate(self.order):
            print(f"{i}. Customer: {order.customer} | {order.name} - Price: {order.total_price()} - Add-on: {order.addon}")
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
            print(" 1.   Show order \n 2.   Add order    \n 3.   Delete order  \n 4.   Delete all orders  \n 5.   Exit Choices and Shift")
            Choice = input("Choice:")
            if Choice == "1":
                manager.orderList()
            elif Choice == "2":
                customer = input("Input customer name: ")
                print("Available coffee: \n 1. Espresso (15000)\n 2. Latte (20000)\n 3. Cappuccino (25000)\n 4. Americano (18000)")
                ordered = input("Input order Name: ")
                if ordered == "1":
                    name = "Espresso"
                    price = 15000
                elif ordered == "2":
                    name = "Latte"
                    price = 20000
                elif ordered == "3":
                    name = "Cappuccino"
                    price = 25000
                elif ordered == "4":
                    name = "Americano"
                    price = 18000
                else:
                    print("Coffee is not available; please choose a valid option.")
                    continue

                print("Available add-on: \n 1. Extra Shot (+3000)\n 2. Soy Milk (+5000)\n 3. Vanilla Syrup (+2000)\n 4. Caramel Syrup (+2000) \n 5. No add-on")
                addonchoice = input("Input add-on number: ")
                addon = "No add-on"
                if addonchoice == "1":
                    addon = "Extra Shot"
                    price += 3000
                elif addonchoice == "2":
                    addon = "Soy Milk"
                    price += 5000
                elif addonchoice == "3":
                    addon = "Vanilla Syrup"
                    price += 2000
                elif addonchoice == "4":
                    addon = "Caramel Syrup"
                    price += 2000
                elif addonchoice == "5":
                    addon = "-"
                    price += 0
                else:
                    print("Add-on is not available; using No add-on")

                manager.Add_order(Order(customer, name, [price], addon))
                print("Order added")
                print(f"Customer : {customer}, Order: {name}, Price: {price}, Add-on: {addon}")

            elif Choice == "3":
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
            elif Choice == "4":
                manager.orderList()
                confirm = input("Are you sure you want to delete all orders? (yes/no): ")
                if confirm.lower() == "yes":
                    manager.DeleteorderAll()
                    print("All orders deleted")
                else:
                    print("Operation cancelled")
            elif Choice == "5":
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
        break


if __name__ == "__main__":
    Main()
