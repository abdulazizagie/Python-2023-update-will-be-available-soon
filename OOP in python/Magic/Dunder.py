class Employee2:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        i = 0
        for c in range(self.name):
            i = i+1
        return i
    # def __str__(self):
        # return f"The name of the employee is {self.name}"
    def __repr__(self):
        return f"The name of the employee is {self.name}"
# e = Employee2("Harry")        
# print(e.name)