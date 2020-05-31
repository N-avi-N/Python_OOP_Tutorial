class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comp.com'

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)


emp_1 = Employee('abc', 'xyz', 50000)  # instance 1 of class
emp_2 = Employee('def', 'ust', 60000)  # instance 2 of class

# print(emp_1)
# print(emp_2)

# emp_1.first = 'abc'
# emp_1.last = 'xyz'
# emp_1.email = 'abc.xyz@comp.com'
# emp_1.pay = 50000
#
# emp_2.first = 'def'
# emp_2.last = 'ust'
# emp_2.email = 'def.ust@comp.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print('{}, {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())

print(emp_1.fullname())
print(Employee.fullname(emp_1))