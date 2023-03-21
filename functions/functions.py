#definīcija
def sareizinat_ar_2(x):
    return x * 2
#izsaukt/call
print(sareizinat_ar_2(5))

def say_hello_to(name):
    print(f"hello {name}!")
say_hello_to('Elizabete')
say_hello_to('Anna')

def say_something():
    print('Something')

say_something()

def sum_of_two_numbers(number1, number2):
    return number1 + number2

print(sum_of_two_numbers(4, 5))

def convert_to_celsius():
    user_value = float(input('Temperature in F: '))
    return (user_value - 32) * 5/9

print(convert_to_celsius())



def convert_to_celsius(temp_f):
    return (temp_f - 32) * 5/9

user_value = float(input('Temperature in F: '))
print(convert_to_celsius(user_value))