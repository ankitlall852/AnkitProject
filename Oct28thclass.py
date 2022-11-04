#Create a calculator
#the else has to be within the if
# a= int(input("enter first no "))
# b = int(input("enter second no "))
# print("press:")
# print("+ for addition ")
# print("- for difference ")
# print("* for difference ")
# print("/ for difference ")
# print("x for exit")
# n = input()
# if(n=='+'):
#     print("addition ")
#     n=a+b
#     print(n)
# else:
#     if(n=="-"):
#         print("difference")
#         n = a-b
#         print(n)
#     else:
#         if(n=="*"):
#             print("Multipy")
#             n=a*b
#             print(n)
#         else:
#             if(n=="/"):
#                 print("DIivsion")
#                 n=a/b
#                 print(n)


#Create a calculator that runs over and over
#We used a while loop
def calc(n):

    if (n == '+'):
        print("addition ")
        n = a + b
        print(n)
    else:
        if (n == "-"):
            print("difference")
            n = a - b
            print(n)
        else:
            if (n == "*"):
                print("Multipy")
                n = a * b
                print(n)
            else:
                if (n == "/"):
                    print("DIivsion")
                    n = a / b
                    print(n)

a= int(input("enter first no "))
b = int(input("enter second no "))
n=""
while(n!="x"):
    print("press:")
    print("+ for addition ")
    print("- for difference ")
    print("* for difference ")
    print("/ for difference ")
    print("x for exit")
    n = input()
    calc(n)

#get button r to redo it ex enter first an enter secon
def calc(n):

    if (n == '+'):
        print("addition ")
        n = a + b
        print(n)
    else:
        if (n == "-"):
            print("difference")
            n = a - b
            print(n)
        else:
            if (n == "*"):
                print("Multipy")
                n = a * b
                print(n)
            else:
                if (n == "/"):
                    print("DIivsion")
                    n = a / b
                    print(n)

a= int(input("enter first no "))
b = int(input("enter second no "))
n=""
while(n!="x"):
    print("press:")
    print("+ for addition ")
    print("- for difference ")
    print("* for difference ")
    print("/ for difference ")
    print("x for exit")
    n = input()
    calc(n)
    if(n=="r"):
        a = int(input("enter first no "))
        b = int(input("enter second no "))
        n = ""
#create r using a function input
