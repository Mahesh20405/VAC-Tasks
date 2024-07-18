class Student:
    def __init__(self, name, reg_no, m1, m2, m3):
        self.name = name
        self.reg_no = reg_no
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def __str__(self):
        return f"Name: {self.name}, Reg No: {self.reg_no}, ms: {self.m1}, {self.m2}, {self.m3}"

    
nos = int(input("Enter n"))
studict = {}
for i in range(nos):
    name = input(f"Enter name {i+1}: ")
    reg_no = input(f"Enter reg.no{i+1}: ")
    m1 = float(input(f"Enter m1 for student {i+1}: "))
    m2 = float(input(f"Enter m2 for student {i+1}: "))
    m3 = float(input(f"Enter m3 for student {i+1}: "))
    student = Student(name, reg_no, m1, m2, m3)
    studict[f"Student {i+1}"] = student

print("Students Dict:")

for key, value in studict.items():
    print(f"{key}: {value}")
