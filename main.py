class Employee:

    # Initializing (Constructor)
    def _init_(self):
        print('Employee created.')

        # Deleting (Destuctor)
        def _del_(self):
            print('Destructor called, Employee deleted. ')

obj = Employee()
del obj            

