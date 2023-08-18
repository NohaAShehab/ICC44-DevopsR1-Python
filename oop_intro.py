# info =['ahmed', 'iti']
# myinfo= {"name":"ahmed","work":"iti"}

# emp1 = {"id": 1, "name": "ahmed", 'salary': 1000}
# emp2 = {"emp_id": 2, "emp_name": "mohamed", 'emp_salary': 2000}

""" create our own datatype ---> object factory --> create objects with same properties , 
apply the same methods"""

# print("ali".upper())
# print('tesrt'.upper())

"1- define a class -->"

# class Employee:
#     pass
#
# "2- take object from the class "
#
# emp = Employee()  # reserve new address in the memory --> type Employee
#
# "3- you populate object with data in the runtime"
# "object.propertyname= value "
# emp.id =1
# emp.name= 'ahmed'
# emp.salary= 1000
#
# "4- print properties of the object "
# print(emp.name)
# print(emp.__dict__)  # represent object properties in form of dict
#
# "5- create new object "
# emp2 = Employee()
# emp2.emp_id = 1
# emp2.emp_name='ali'
# emp2.salary=10000
#
# "6- check if object from class ? "
# print(isinstance(emp, Employee))
# print(isinstance(emp2, Employee))

" define unified architecture for  the object "
#
# class Employee:
#     # constructor  -->
#     def  __init__(self):  # self ?
#         # print("""--- object is being created,
#         # this function is being called while creating object ----------""")
#         print(f'object is being created {self}')  # self --: represent object address in the memory
#         self.id =1
#         self.name= 'ahmed'
#         self.salary= 1000
#
#
# emp1 = Employee()  # create new object --> call function --> in the class __init__
# print(f'emp1= {emp1}')
# # (constructor function) --> is being called while creating the object
# emp2 = Employee()
# print(f"emp2= {emp2}")
# print(emp2.name)
# emp2.name ='updated'

""" customize object while creating """

# class Employee:
#     # constructor : customize object properties while creation  -->
#     def  __init__(self, userid=1, empname='name__' , empsalary=1000):  # self ?
#         "id , name, salary 00> instance variables ==> their value depends on the caller instance "
#         self.id =userid
#         self.name= empname
#         self.salary= empsalary
#
# emp1 = Employee()
# print(emp1.name)
# emp = Employee(10, 'omar', 10000)
# print(emp.name)
# emp2 = Employee(70, 'test', 2999)
# emp2.email = 'ahmed@gmail.com'


"""add behaviour --> functionality/ action that instance from this class can do """

""" instance methods ---> """
#
# class Employee:
#     def  __init__(self, userid=1, empname='name__' , empsalary=1000):  # self ?
#         "id , name, salary 00> instance variables ==> their value depends on the caller instance "
#         self.id =userid
#         self.name= empname
#         self.salary= empsalary
#
#     def employeeInfo(self , message):  # instance method --->
#         print(f"id={self.id}, name={self.name}, salary={self.salary}, {message}")
#
#     """ when you create instance method  --> python consider the first parameter to
#     represent address of the object  --> self"""
#     def myfun(iti):  # usually first parameter of method is named self --> represent object address
#         print(iti)
#
# emp1 = Employee()
# emp1.employeeInfo("hii")
#
# emp2 = Employee(2, 'fady', 500)
# emp2.employeeInfo("bye")
#
# emp2.myfun()
""" class variable """
""" property represent class not the instance """

# class Employee:
#     count = 0  # class variable --> represent property related to the class not the instance
#     happy = True
#
#     def __init__(self, userid=1, empname='name__', empsalary=1000):  # self ?
#         self.id = userid
#         self.name = empname
#         self.salary = empsalary
#         # self.__class__.count +=1
#         Employee.count += 1
#
#     def employeeInfo(self, message):  # instance method --->
#         print(f"id={self.id}, name={self.name}, salary={self.salary}, {message}")
#
#
# emp1 = Employee()
# emp1.employeeInfo("hii")
#
# emp2 = Employee(2, 'fady', 500)
# emp2.employeeInfo("bye")
#
# # ## access class variable
# print(Employee.count)
# print(emp1.__dict__)

""" class method """

#
# class Employee:
#     count = 0  # class variable --> represent property related to the class not the instance
#     happy = True
#
#     def __init__(self, userid, empname, empsalary):  # self ?
#         self.id = userid
#         self.name = empname
#         self.salary = empsalary
#         # self.__class__.count +=1
#         Employee.count += 1
#
#     def employeeInfo(self, message):  # instance method --->
#         print(f"id={self.id}, name={self.name}, salary={self.salary}, {message}")
#
#     """ method represent behaviour  --> depends on the class not the instance"""
#
#     @classmethod  # # first argument of the function represent class not the instance
#     def get_emp_count(cls, message):  # cls  --> current class
#         print(f'cls= {cls}, {message}')
#         # return Employee.count
#         return cls.count
#
#     # consider class method to be object factory
#     @classmethod
#     def create_default_object(cls):
#         return cls(1, 'default', 1000)
#
#     # ## save to a file ? instance  --->
#     def save_to_file(self):
#         data_to_save = self.__dict__
#
#     # # load all employees from file ?
#     @classmethod  # decorator
#     def load_employees(cls):
#         print(cls)
#
#
# emp = Employee.create_default_object()
# Employee.load_employees()
# # emp = Employee(1, 'rrr', 30495)
# # emp2 = Employee.create_default_object()

""" static method """

class Employee:
    count = 0  # class variable --> represent property related to the class not the instance
    happy = True

    def __init__(self, userid, empname, empsalary):  # self ?
        self.id = userid
        self.name = empname
        self.salary = empsalary
        # self.__class__.count +=1
        Employee.count += 1

    def employeeInfo(self, message):  # instance method --->
        print(f"id={self.id}, name={self.name}, salary={self.salary}, {message}")

    """ method represent behaviour  --> depends on the class not the instance"""

    @classmethod  # # first argument of the function represent class not the instance
    def get_emp_count(cls, message):  # cls  --> current class
        print(f'cls= {cls}, {message}')
        # return Employee.count
        return cls.count

    # consider class method to be object factory
    @classmethod
    def create_default_object(cls):
        return cls(1, 'default', 1000)

    # ## save to a file ? instance  --->
    def save_to_file(self):
        data_to_save = self.__dict__

    # # load all employees from file ?
    @classmethod  # decorator
    def load_employees(cls):
        print(cls)

    @staticmethod # decorator --> function --> doesn't depend on class or instance
    # helper method  ---> can be called using instance or class
    def cal_net_sal(salary):
        return salary * .8


emp = Employee.create_default_object()
print(emp.salary)
print(emp.cal_net_sal(emp.salary))
print(Employee.cal_net_sal(emp.salary))
print(Employee.cal_net_sal(4564332))
# def cal_net_sal(salary):
#     return salary*.8

# print(cal_net_sal(emp.salary))
#
# print(cal_net_sal(10000000))