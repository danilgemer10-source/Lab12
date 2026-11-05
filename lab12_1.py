import random

def first_function(text, n):
    
    for i in range(0, len(text), n):
        print(text[i:i+n])
        
text = input("Введіть текст: ")
n = int(input("Введіть кількість символів: "))
first_function(text, n)

print()

def second_function(text):
    
    for i in range(0, len(text), 2):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        print(text[i:i+2] + str(num1) + str(num2))
        
        
text = input("Введіть текст: ")
second_function(text)