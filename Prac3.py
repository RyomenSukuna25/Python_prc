class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format(self.designation)
    
    def verifier (self):
        if self.frontend and self.backend:
            print("The person is a Fullstack Developer")
        elif self.frontend:
            print("The person is a Frontend Developer")
        elif self.backend:
            print("The person is a Backend Developer")
        else:
            print("The person is not a Developer")

if __name__ == '__main__':
    firstEmployee = Employee(frontend=True, backend=True)
    firstEmployee.verifier() 

    secondEmployee = Employee(frontend=True)
    secondEmployee.verifier()

    thirdEmployee = Employee(backend=True)
    thirdEmployee.verifier()
    
    fourthEmployee = Employee()
    fourthEmployee.verifier()

# Chirag Nagvekar, SE2, 64