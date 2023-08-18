
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self.email = email
#         self.salary =salary
#
#     def print_emp_info(self):
#         print(self.name)
#
#
# class Engineer(Employee):
#     pass
#
# eng1 = Engineer("ahmed","ahmed@gmail", 10000)
# print(isinstance(eng1, Employee))
# eng1.print_emp_info()

######################3

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self.email = email
#         self.salary =salary
#
#     def print_emp_info(self):
#         print(self.name)
#
#
# class Engineer(Employee):
#     def __init__(self, name, email, salary, sepialization):
#         # call parent __init__
#         super().__init__(name, email, salary)
#         self.specialization  = sepialization
#
#
# eng1 = Engineer( 'ahmed', 'ahmed@gmail',1000, 'cs')
# print(isinstance(eng1, Employee))
# eng1.print_emp_info()



""" ---------> inhertiance ---> overriding """

class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary =salary

    def print_emp_info(self):
        print(self.name)


class Engineer(Employee):
    def __init__(self, name, email, salary, sepialization):
        # call parent __init__
        super().__init__(name, email, salary)
        self.specialization  = sepialization

    # overriding --> 2 methods in 2 classes (inheritance relation )
    def print_emp_info(self):
        super().print_emp_info()
        print(self.specialization)

eng1 = Engineer( 'ahmed', 'ahmed@gmail',1000, 'cs')
print(isinstance(eng1, Employee))
eng1.print_emp_info()









