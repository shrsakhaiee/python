import math
while True:
    op = input()
    if op == "exit":
        break
    if op =="sin" or op == "log" or op =="tan" or op =="cot" or op == "fact" :
        a = int(input())
    else:
        a = int(input())
        b = int(input())

    if op == "+":
        result = a+b
    elif op == "-":
        result = a-b
    elif op == "*":
        result = a*b
    elif op == "/":
        if b != 0 :
         result = a/b  
        else : 
         result = "cannot divide by zero"
    elif op == "^":
         result = a**b
    elif op =="sin":
        result = math.sin(a)
    elif op == "log":
        result = math.log10(a)
    elif op =="tan":
        result = math.tan(a)
    elif op == "cot":
        result = 1/math.tan(a)
    elif op == "fact":
        result = math.factorial(a)
    else: 
        result = "nmifahmam chi migi :/ khodanegahdar"

    print (result)