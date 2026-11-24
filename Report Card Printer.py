name = input('Enter the name: ')
print(name, type(name))

is_student = input('Is the person a student? (True/False): ')
is_student = bool(is_student)
print(is_student, type(is_student))

age = int(input('Enter the age: '))
print(age, type(age))

score = float(input('Enter the score: '))
print(isinstance(score, float)
