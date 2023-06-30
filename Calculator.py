class Calculator:

    def __init__(self, num1, num2):
        self.num1 = None
        self.num2 = None
        self.result = None

    def add(self, num1, num2):


        self.result = num1 + num2 

    def sub(self, num1, num2):
        self.result = num1 - num2

    def mul(self, num1, num2):
        self.result = num1 * num2

    def div(self, num1, num2):
        self.result = num1 // num2
    
    
    def get_result(self):

        return self.result


        