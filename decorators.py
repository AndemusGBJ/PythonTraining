def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout
print(yell('Hello'))


def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)


def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))



# Decoratos

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")
        
    return inner1

def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()


def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")

        returned_value = func(*args, **kwargs)
        print("after Execution")

        return returned_value
        
    return inner1

@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2

print("Sum =", sum_two_numbers(a, b))


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 2

@decor2
@decor1
def num2():
    return 2

print(num())
print(num2())


### EXERCISES
"""
1.
write a function named greet(func)

inside greet(func) create another function that does the following:
	1. print something
	2. a variable that uses func to access different arguments (*args)

define another function called say_hello() which prints something
and by calling say_hello() at the end, also the greet(func) should be
provoked.
"""

def greet(func):
    def inner(*args):
        print("Hello")
        a = func(*args)
        return a
    return inner

def say_hello():
    return "Hello again"
print("Exercise 1")
greet(say_hello)()

"""
2.
write a function called authorize(func)
define a wrapper (func inside another func) inside and return
"Unathorized access" if not authorized.
define another function to check whether authorized or not. (True or False)
define the last function named secret_data() 
to say "This is confidential data" if user is authorized.
By calling secret_data you should see if the data is confidential or 
you will provoke the other function that says "Unauthorized access".
"""

def authorize(func):
    def wrapper(*args):
        if check_auth():
            return func()
        else:
            return "Unauthorized access"
    return wrapper

def check_auth(*args):
    return True

@authorize
def secret_data():
    return("This is confidential data")
    
print(secret_data())

"""
1.
write a function that yields the first 10 prime numbers.

Tips:
	you need 2 functions (is_prime() and prime_numbers(n)) 
	
prime_generator = prime_numbers(10)
print(list(prime_generator))

# output should be:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    
def prime_numbers(n):
    i=2
    a=0
    while True:
        if is_prime(i):
            yield i
            a+=1
        i+=1 
        
        if a == n:
            break
        


prime_generator = prime_numbers(10)
print(list(prime_generator))


##Checkk emails in filex

def emails_in_line(text):
    with open(text) as text:
        lines = text.read().splitlines()
    for i in range(len(lines)):
        if '@' in lines[i]:
            yield lines[i]

line = emails_in_line('file.txt')
while True:
    print(next(line))
    next_prime = input(' Next ine with @ is : ').strip().lower()
    if next_prime == 'e':
        break