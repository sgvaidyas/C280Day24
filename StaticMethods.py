class Calculate:
    @staticmethod
    def Add_num(a, b): # define the static Math_num() function
        return a + b

    @staticmethod
    def Sub_num(a, b): # define the static Sci_num() function
        return a -b

    @staticmethod
    def Mul_num(a, b):  # define the static Eng_num() function
        return a*b

# print the total marks in Maths
print (" ADD          " , Calculate.Add_num(64, 28))
# print the total marks in Science
print (" SUB          " , Calculate.Sub_num(70, 25))
# print the total marks in English
print (" MUL          " , Calculate.Mul_num(65, 30))
