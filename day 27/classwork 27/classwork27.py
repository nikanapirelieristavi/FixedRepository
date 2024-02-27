# 3)პითონში უნდა შექმნათ მათემატიკური პროგრამა სადაც მომხარებელს შეეძლება აირჩიოს რომელი მათემატიკური ფუნქცია , +,-./,*. 
# სულ შეიძლება 2 რიცხვის შეტანა და შემდეგ დაუბრუნე პასუხი. 
a = 0
b = 0
x = int(input())
y = int(input())
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        print("invalid")
def calculator():
    print("choose two numbers:")
    print(x)
    print(y)
    a += x
    b += y
    print("choose an operation:")
    print("add")
    print("substract")
    print("multiply")
    print("divide")
    
    choice = 1, 2, 3, 4
    
    print("choose either ", choice)

    if choice == 1:
        print(add(a, b))
    elif choice == 2:
        print(sub(a, b))
    elif choice == 3:
        print(mult(a, b))
    elif choice == 4:
        print(div(a, b))
    
calculator()

    