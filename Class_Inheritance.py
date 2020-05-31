
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comp.com'

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)              # lets us inherit from the parent class
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('abc', 'xyz', 50000)
emp_2 = Employee('def', 'ust', 60000)

print(emp_1.email)
print(emp_2.email, '\n')

dev_1 = Developer('abc', 'xyz', 50000, 'python')
dev_2 = Developer('def', 'ust', 60000, 'java')

# print(help(Developer))

print(dev_1.email)
print(dev_1.prog_lang, '\n')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))