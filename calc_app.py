import pyinputplus as pyip

# num1 = pyip.inputNum(prompt = "Enter first num: ")
# num2 = pyip.inputNum(prompt = "Enter second num: ")
# op = input("Enter operation: ")

def add(n1, n2):
  return (n1 + n2)

def subtract(n1, n2):
  return (n1 - n2)

def multiply(n1, n2):
  return (n1 * n2)

def divide(n1, n2):
  if n2 == 0:
    return "Cannot divide by 0"
  else:
    return (n1/n2)

# if op == "+":
#     add(num1, num2)
# elif op == "-":
#     subtract(num1, num2)
# elif op == "*":
#     multiply(num1, num2)
# elif op == "/":
#     divide(num1, num2)
# else: 
#     print("Invalid input")

    