#function=wrtie code once and use it anywhere
#is a block of code
# used for reusability.
#ex def x(
 #code inside here)
#when we use it its x()


#Advanced functions

#Homework print 3 functions goodmorning,goodevening and goodnight
#Goodmorning with value,goodevening with value and goodnight with value
# def gm(a):
#     print("good morning"+" " + a)
# gm("Ankit")
# def ge(b):
#     print("good evening"+" " + b)
# ge("Sam")
# def ge(c):
#     print("good night"+" " + c)
# ge("Saddam")

#Same as above but within 1 parenthesis
# def gm(a,b):
#     print("goodmorning"+" "+a+b)
# # def ge(a,b):
# # #     print("goodevening"+a+b)
# def final():
#     (gm(),ge())
# gm("ankit","saddam hussien")

def canVote(username,age):
    if(age>=18 and age<=120):
        print(username+" you are eligible for voting")
        if(age<=0):
        print(username+"you are not eligible for voting")
    else:
        print("too old")
    else:
        print(username+ " you are not eligible for voting")

n = input("enter your name")
a = int(input("enter your age"))
canVote(n,a)

