import json

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def print_intro(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}")
    
    def increment(self, increment):
        self.salary += increment
        print(f"Salary after increment: {self.salary}")        
        
    def save_to_json(self, filename):
        employee_dict = {
            'name': self.name,
            'age': self.age,
            'salary': self.salary
        }
        with open(filename, 'w') as f:
            json.dump(employee_dict, f, indent=4)  # Use json.dump, not json.dumps
    
    def load_to_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)  # Use json.load, not json.loads
            self.name = data['name']
            self.age = data['age']
            self.salary = data['salary']
            print(f"Employee loaded from file: {self.name}")
            
# Testing the code
# Save employee data
# e1 = Employee('bob', 20, 300)
# e1.print_intro()
# e1.save_to_json('bob.json')
# e1.increment(10000)
# e1.print_intro()

# Load employee data from file
e2 = Employee(None, None, None)
e2.load_to_json('bob.json')
e2.print_intro()
