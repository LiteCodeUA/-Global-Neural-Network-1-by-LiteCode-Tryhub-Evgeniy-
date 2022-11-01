import math
print("Welcome to GlobalNeuralNetwok by LiteCode (Tryhub Evgeniy)")


#functions_sys
F1 = input("+ / - ?:")


#info
i1 = input("first number:")
i2 = input("second number:")


#weight
w1 = print(i1)
print ("created weight: 1")

w2 = print(i2)
print ("created weight: 2")


#neyron and answer (x = perceptron)
print("F=(perceptron [weight] in neyron)")
if F1 == "+":
    x = i1 + i2
print("answer:" + x)   

print("F=(perceptron [weight] in neyron)")
if F1 == "-":
    x = i1 - i2
print("answer:" + x)

