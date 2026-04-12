import csv

class menu:
    # nama dan price
    def __init__(self, coffee, price):
        self.coffee = coffee
        self.price = price

class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def average(self):
        if not self.price:
            return 0
        return sum(self.price) / len(self.price)

class Reportorder:
    def __init__(self, filename = "ORDER.csv"):
        self.order = []
        self.filename = filename
        self.loadFile()
    
    def loadFile(self):
        self.order.clear()
        try:
            with open (self.filename, newline= "" ) as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    price = list(map(int, row[1: ]))
                    self.order.append(Order(name, price))
        except FileNotFoundError:
            print("File", self.filename, "not found. Create new file!!!")
    
    def saveFile(self):
        with open(self.filename, "w", newline= "") as file:
            writer = csv.writer(file)
            for order in self.order:
                writer.writerow([order.name] + order.price)
        
    # def add order
    def Add_order(self, order):
        self.order.append(order)
        # simpan data
        self.saveFile()
        
    def orderList(self):
        if not self.order:
            print("Tidak ada data")
            return
        print("DAFTAR SISWA:")
        for i, order in enumerate(self.order):
            print(f"{i}. {order.name} - Price: {order.price}")
        print()

    def Deleteorder(self, index):
        del self.order[index]
        self.saveFile()
    
       
def Main():
    manager = Reportorder()
    
    
    while True:
        print("Pleasee pick the following choices:")
        print(" 1.   Show order \n 2.   Add order    \n 3.   Delete order  \n 4.   Exit Choices")
        Choice = input("Choice:")
        if Choice == "1":
            manager.orderList()
        elif Choice == "2":
            name = input("Input order Name: ")
            price = input("Input order price total: ")
            try:
                price = list(map(int,price.split(",")))
                manager.Add_order(Order(name, price))
                print("Order berhasil ditambahkan")
            except ValueError:
                print("Input a real price!!")
             

        elif Choice == "3":
            manager.orderList()
            try:
                index = int(input("Masukkan Nomor Order yang ingin dihapus= "))
                if 0 <= index < len(manager.order):
                    manager.Deleteorder(index)
                    print("Order berhasil dihapus")
            except ValueError:
                    print("Order tidak ditemukan")
        elif Choice == "4":
            print("Terima Kasih telah menggunakan program ini")
            break
        
    
    
Main()
