
def U3Task1():
    print("Решение задачи №1: \n")



def U3Task2():
    print("Решение задачи №2: \n")



def U3Task3():
    print("Решение задачи №3: \n")



def U3Task4():

    print("Решение задачи №4: \n")
    num = int(input('Enter how many numbers needed in Fibonacci series: '))

    LstNum = []
    LstFib = []
    num1, num2 = 0, 1
    fib1, fib2 = 0, 1
    for i in range(num):
        num1, num2 = num2, num1 + num2
        LstNum.append(num1)
        fib1, fib2 = fib2, fib1 - fib2
        LstFib.append(fib1)
    LstFib.reverse()
    print(f'Негафиббоначи: {[*LstFib, 0, *LstNum]}')

