class Employee:
    total_employees = 0
    total_salary = 0

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        Employee.total_employees += 1
        Employee.total_salary += salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        Employee.total_salary -= self.salary
        self.salary = new_salary
        Employee.total_salary += new_salary

    @classmethod
    def average_salary(cls):
        if cls.total_employees > 0:
            return cls.total_salary / cls.total_employees
        else:
            return 0

# Create some Employee instances
employee1 = Employee("Ali", 101, 50000)
employee2 = Employee("Ram", 102, 60000)
employee3 = Employee("Raj", 103, 75000)

# Get and set salaries
print("Employee 1's current salary:", employee1.get_salary())
employee1.set_salary(55000)
print("Employee 1's updated salary:", employee1.get_salary())

# Calculate average salary
print("Average Salary of all employees:", Employee.average_salary())
