#1. Create an Employee class with a class variable company = "TechCorp" and instance variables name and role. Create three employees and print each one's company and name.
class Employee:
    company = "TechCorp"
    def __init__(self, name, role):
        self.name = name
        self.role = role

employee1 = Employee("Alu", "Software Engineer")
employee2 = Employee("Bobbu", "Data Analyst")
employee3 = Employee("Charlieu", "Product Manager")

print(f"Company: {Employee.company}")
print(f"Employee 1: {employee1.name}")
print(f"Employee 2: {employee2.name}")
print(f"Employee 3: {employee3.name}")

#2. Add an employee_count class variable that increments each time an employee is created. Print the total after creating three employees.
class Employee:
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.employee_count += 1

employee1 = Employee("Aashu", "Software Engineer")
employee2 = Employee("Bobbi", "Data Analyst")
employee3 = Employee("Char", "Product Manager")

print(f"Company: {Employee.company}")
print(f"Employee 1: {employee1.name}")
print(f"Employee 2: {employee2.name}")
print(f"Employee 3: {employee3.name}")
print(f"Total employees: {Employee.employee_count}")

#3. Experiment with the pitfall: create two objects, change the class variable through one instance, and observe what happens to the other instance and the class itself.
class Employee:
    company = "TechCorp"
    def __init__(self, name, role):
        self.name = name
        self.role = role
employee1 = Employee("Shivanz", "Software Engineer")
employee2 = Employee("Atharv", "Data Analyst")

print(f"Company before change: {Employee.company}")
print(f"Employee 1: {employee1.company}")
print(f"Employee 2: {employee2.company}")

# Change the class variable through one instance
employee1.company = "NewTechCorp"
print(f"Company after change: {Employee.company}")
print(f"Employee 1's company: {employee1.company}")
print(f"Employee 2's company: {employee2.company}")