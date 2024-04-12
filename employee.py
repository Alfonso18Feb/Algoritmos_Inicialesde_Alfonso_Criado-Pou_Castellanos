

class Employee():
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
     obj= Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.

    def __init__(self,emp_id, name, position, salary):
        self.emp_id=emp_id             
        self.name=name
        self.position=position
        self.salary=salary
    def get_name(self):
        if isinstance(self.name, str):
            return self.name
        else:
            TypeError("you need to write his name")
    def get_emp_id(self):
        if isinstance(self.emp_id,int):
             return self.emp_id
        else:
            TypeError('')
    def get_position(self):
        if isinstance(self.position,str):
            return self.position
        else:
            TypeError('it need to be one of the above Recepcionista, Limpiador, Gerente, etc ')

    def get_salary(self):
        if isinstance(self.salary,float):
            if self.salary>1000:
                return self.salary
            else:
                ValueError('Not paying minimum wage')
        else:
            TypeError('It needs to be a number')
    def set_position(self,position):
        self.position=position
    def set_salary(self,salary):
        self.salary=salary
    def __str__(self) -> str:
        return 'employee id \n'+str(self.emp_id)+'his name is \n'+str(self.name)+'his position is\n '+str(self.position)+'his salary is of\n'+str(self.emp_id)

def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
