import csv

class student:
    # nama dan score
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # nilai rata-rata
    def average(self):
        return sum(self.score) / len(self.score) if self.score else 0
      

# add student, read, delete, find
class ReportStudent:
    def __init__(self, filename = "student.csv"):
        self.students = []
        self.filename = filename
        self.loadFile()
    
    def loadFile(self):
        self.students.clear()
        try:
            with open (self.filename, newline= "" ) as file:
                reader = csv.reader(file)
                for row in reader:
                    name = row[0]
                    score = list(map(int, row[1: ]))
                    self.students.append(student(name, score))
        except FileNotFoundError:
            print("File", self.filename, "not found. Create new file!!!")
    
    def saveFile(self):
        with open(self.filename, "w", newline= "") as file:
            writer = csv.writer(file)
            for student in self.students:
                writer.writerow([student.name] + student.score)
        
    # def add student
    def Add_Student(self, student):
        self.students.append(student)
        # simpan data
        self.saveFile()
        
    def studentList(self):
        if not self.students:
            print("Tidak ada data siswa")
            return
        print("DAFTAR SISWA:")
        for i, student in enumerate(self.students):
            print(f"{i}. {student.name} - Nilai: {student.score} - Rata-rata: {student.average():.2f}")
        print()

    def DeleteStudent(self, index):
        del self.students[index]
        self.saveFile()
    
       
def Main():
    manager = ReportStudent()
    
    
    while True:
        print("Pleasee pick the following choices:")
        print(" 1.   Show Student \n 2.   Add Student    \n 3.   Delete Student  \n 4.   Exit Choices")
        Choice = input("Choice:")
        if Choice == "1":
            manager.studentList()
        elif Choice == "2":
            name = input("Input Student Name: ")
            score = input("Input Student Score: ")
            try:
                score = list(map(int,score.split(",")))
                manager.Add_Student(student(name, score))
                print("Siswa berhasil ditambahkan")
            except ValueError:
                print("Input a real score!!")
             

        elif Choice == "3":
            manager.studentList()
            try:
                index = int(input("Masukkan Nomor siswa yang ingin dihapus= "))
                if 0 <= index < len(manager.students):
                    manager.DeleteStudent(index)
                    print("Siswa berhasil dihapus")
            except ValueError:
                    print("Siswa tidak ditemukan")
        elif Choice == "4":
            print("Terima Kasih telah menggunakan program ini")
            break
        
    
    
Main()


# List Menu:
'''
1. Tampilkan siswa
2. Tambah siswa
3. Hapus siswa
4. Cari siswa(opsi)
5. Keluar


'''
        