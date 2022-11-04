#print from 0 to 29
# for i in range (0,30):
#     print(i)
#print from range 12 to 22 in increments of 3
# for i in range (12,22,3):
#     print(i)

#output should be 10,9,8,7,6,5,4,3,2,`
# for i in range (10,0,-1):
#     print(i)

# print all even numbers from 10 to 25 using mods
# for i in range(10,26):
#     if(i%2==0):
#       print(i)

# print all odd numbers from 10 to 25 using mods
# for i in range(10,26):
#     if(i%2==1):
#       print(i)

#Dont print no divisible by both 2 and 5. From 1 to 60
# for i in range(1,60):
#     if(i%2==0 & i%5==0):
#           continue
#     print(i)

#print 1,2,3,4,5,up to 10.
#take number from user, and take end of list.
#first variable &, and second variable
#print all numbers in between
#2)take list 1 to 50. If no is divisble by 2,
#it should say put if divisible by 2,
#get if no is divisble by 5
#if no is divisble by both 2 and 5, well

#Question : how do i print if greater than 10 invalid no
# a=int(input("input a number between 1 and 10"))
# b=int(input("input a number between 1 and 10"))
# for i in range(a,b):
#     if(i>1 and i<10):
#         print(i)

#same code as above but with error message if above 10
# a=int(input("input a number between 1 and 10"))
# b=int(input("input a number between 1 and 10"))
# if(a>10 or b>10):
#     print(("Please enter no's less than 10"))
# else:
#     for i in range(a,b):
#         if(i>1 and i<10):
#     print(i)
#




#2)take list 1 to 50. If no is divisble by 2,
#it should say put if divisible by 2,
#get if no is divisble by 5
#if no is divisble by both 2 and 5, well

# for i in range(1,50):
# if(i%2==0):
#     print(i)
#      print("put")
# else(i%5==0):
#     print("get")
# else(i%2==0 and i%5==0):
#     print("well")
# print(i)

##2)take list 1 to 50. If no is divisble by 2,
#it should say put if divisible by 2,
#get if no is divisble by 5
#if no is divisble by both 2 and 5, well
for i in range(1,50):
    if(i%2 ==0 and i%5==0):
        print(str(i)+"well")
    else:
        if(i%2==0):
            print(str(i)+"put")
        else:
            if(i%5==0):
                print(str(i)+"get")
            else:
                print(i)
#my code 
    #  if(i%2==0):
    #           print("put")
    #    if(i%5==0):
    #        print("get")
    #    if(i%2==0 and i%5==0):
    #        print("well")
    # rint(i)p



