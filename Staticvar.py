class Student:
	stream = 'Mechanical'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = Student('Abas', 1)
b = Student('David', 2)
c = Student('Asha', 3)
print(a.stream) # prints "Mechanical"
print(b.stream) # prints "Mechanical"
print(a.name) # prints "Abas"
print(b.name) # prints "David"
print(a.roll) # prints "1"
print(b.roll) # prints "2"
# Class variables can be accessed using class
# name also
print(Student.stream) # prints "Mechanical"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'Computers'
print(a.stream) # prints 'Computers'
print(b.stream) # prints 'Mechanical'

# To change the stream for all instances of the class we can change it
# directly from the class
Student.stream = 'Electronics'

print("-------------------------")
print(a.stream) # prints 'Computers'
print(b.stream) # prints 'Electronics'
print(c.stream) # prints 'Electronics'
