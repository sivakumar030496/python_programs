# class inputoutstring(object):
#     def __init__(self):
#         self.s=""
#     def getstring(self):
#  =50
# # h=30
# # value=[]
# # items=[x for x in input().split(',')]
# # for d in items:
# #     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# # print(','.join(value))       self.s=input()
#     def printstring(self):
#         print(self.s.upper())
# strobj=inputoutstring()
# strobj.getstring()
# strobj.printstring()

# import math
# c



# input_str=input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist=[[0 for col in range(colNum)] for row in range(rowNum)]
# for col in range(colNum):
#     multilist[row][col]=row*col
# print(multilist)

# print(multi_list)
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
#
# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col
#


#
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))

#
# lines=[]
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)
#
# l=[]
# for i in range(2000,3201):
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))

#
# def fact(x):
#     if x == 0:
#         return 9
# l=values.split()
# t=tuple(l)
# print (l)
# print (t)
#


# input_str =input()
# dimensions=[int (x)for x in input- str. split (',') ]
# rowNum =dimensions[0]
# colNum=dimesions[1]
# multilist =[[0for col in range (colNum)] for row in range(rowNum)]
# for col in range (colNum):
#     multilist[row][col]=row* col
# print (multilist)

# items=[x for x in input(). split(',')]
# items.sort()
# print(','.join(items))

# lines=[]
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)


# s=input()
# words=[word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))

# value=[]
# items=[x for x in input().split(',')]
# for p in items:
#     intp=int(p,2)
#     if not intp%5:
#         value.append(p)
# print(','.join(value))

# values=[]
# for i in range(1000,3001):
#     s=str(i)
#     if(int(s[0])%2==0) and (int(s[1])%2==0) and(int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

# s=input ()
# d={"DIGITS" : 0,"LETTERS" :0}
# for c in s:
#     if c.isdigit ():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
#     print("LETTERS", d["LETTERS"])
#     print("DIGITS" ,d ["DIGITS"])

# s=input()
# d={"UPPER CASE":0,"LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#          pass
# print("UPPER CASE",d["UPPER CASE"])
# print("LOWER CASE",d["LOWER CASE"])

# a=input()
# n1=int("%s"%a)
# n2=int("%s%s"%(a,a))
# # n3=int("%s%s%s"%(a,a,a))
# # n4=int("%s%s%s%s"%(a,a,a,a))
# print (n1+n2)

# values=input()
# numbers=[x for x in values.split(",") if int(x)%2!=0]
# print(",".join(numbers)

# netamount=0
# while True:
#     s=input()
#     if not s:
#         break
#     values=s.split(" ")
#     operation=values[0]
#     amount=int(values[1])
#     if operation=="D":
#         netamount+=amount
#     elif operation=="W":
#         netamount-=amount
#     else:
#         pass
# print(netamount)

# import re
# value=[]
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("A-Z",p):
#         continue
#     elif not re.search("$#@",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#          pass
#     value.append(p)
# print(",".join(value))

# import string
# x=input()
# values=x.split(',')
# l='$#@'
# lis=[]
# for s in values:
#     d={}
#     if len(s)>=6 and len(s)<=12:
#         d[1]=1
#         for i in s:
#             if i in string.ascii_lowercase:
#                 d[2]=1
#             if i in string.ascii_uppercase:
#                 d[3]=1
#             if i in string.digits:
#                 d[4]=1
#             if i in l:
#                 d[5]=1
#             else:
#                 pass
#         sum=0
#         for i in d.values():
#             sum+=1
#         if sum==5:
#             lis.append(s)
# print(lis)

# freq={}
# line=input()
# for word in line.split():
#     freq[word]=freq.get(word,0)+1
# words=freq.keys()
# words.sorted()
# for word in words:
#     print("%s:%d"%(w,freq[w]))

#
# import collections
# s=input()
# x=s.split()
# m=collections.Counter(x)
# print(m)


# def square(num):
#     return num ** 2
# print(square(2))
# print(square(3))

# print (abs.doc)
# print (int.doc)
# print (input.doc)

# def square(num):
#     return num**2
#
# print(square(2))
# print(square.__doc__)

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(num):
#     return num**2
# print (square(2))
# print(square.__doc__)

# class person:
#     name='person'
#     def __init__(self,name=  None):
#         self.name=name
# jeffrey=person("Jeffrey")
# print("%s name is %s"%(person.name,jeffrey.name))

# def sumfunction(number1,number2):
#     return number1+number2
# print(sumfunction)

# def printvalue(n):
#     print(str(n))
# printvalue(3)

# def printtvalue(s1,s2):
#     print (int (s1)+int (s2))
#     printvalue ("3,4")#7

# def printvalue(s1,s2):
#     print (s1+s2)
# printvalue("3" ,"4")#34

# def printvalue(s1,s2):
#     len1=len(s1)
#     len2=len(s2)
#     if len1>len2:
#         print (s1)
#     elif len2>len1:
#         print (s2)
#     else:
#          prin (s1)
#          print (s2)
# printvalue("one","three")

# def checkvalue(n):
#     if n%2==0:
#         print("it is an even number")
#     else:
#         print("it is an odd number")

# def printdict():
#     d=dict()
#     d[1]=1
#     d[2]=2**2
#     d[3]=3**2
#     print(d)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i**2
#     print(d)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i**2
#     for(k,v) in d.items():
#         print(v)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i**2
#     for k in d.keys():
#         print(k)
# printdict()

# def printlist():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li[-5])
# printlist()

# def printlist():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li[5:])
# printlist()

# def printtuple():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (tuple(li))
# printtuple()

# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)

# s=input()
# if s=="Yes" or s=="YES" or s=="Yes":
#     print("Yes")
# else:
#     print("No")
# import pywhatkit
#
# # pywhatkit.sendwhatmsg("+918106009627",
# #                       "I love you!",
# #                       10, 26)
# try:

    # it will perform google search
# pywhatkit.playonyt("srivalli")
# print("Playing...")

#     print("\nSuccessfully Searched")
#
# except:
#
#     # printing error message
#     print("An Unknown Error Occured")

# li=[1,2,3,4,5,6,7,8,9,10]
# evennumbers=map(lambda x:x**2,filter(lambda x:x%2==0,li))
# print (evennumbers)

# l=[]
# for i in range(2000,3201):
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))

# def fact(x):
#     if x==0:
#         return 1
#     return x*fact(x-1)
# x=int(input())
# print(fact(x))

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

## values=input()
# l=values.split
# t=tuple(l)
# print(l)
# print(t)
# ##class inputoutstring(object):
#      def__init__(self):
#      self.s=""
# def getstring(self):
#     self.s=input()
# def printstring(self):
#     print (self.s.upper())
# strobj=inputoutstring()
# strobj.getstring()
# strobj.printstring()

# import math
# c=50
# h=30
# value=[]
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(math.sqrt(2*c*float(d)/h))))
# print(','.join(value))

### input_str=input()
# dimensions=[int(x)for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist=[[0 for col in range(colNum)] for row in range(rowNum)]
# for col in range(colNum):
#     multilist[row][col]=row*col
# print(multilist)

# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))

# lines=[]
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)

# s=input()
# words=[word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))

# value=[]
# items=[x for x in input().split(',')]
# for p in items:
#     intp=int(p,2)
#     if not intp%5:
#         value.append(p)
# print(','.join(value))

# values=[]
# for i in range(1000,3001):
#     s=str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))
#
# s=input()
# d={"DIGITS":0,"LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
#     print("LETTERS",d["LETTERS"])
#     print("DIGITS",d["DIGITS"])
#

# s=input()
# d={"UPPER CASE":0,"LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
#     print("UPPER CASE",d["UPPER CASE"])
#     print("LOWER CASE",d["LOWER CASE"])

# a=input()
# n1=int("%s"%a)
# n2=int("%s%s"%(a,a))
# n3=int("%s%s%s"%(a,a,a))
# n4=int("%s%s%s%s"%(a,a,a,a))
# print(n1+n2+n3+n4)

# values=input()
# numbers=[x for x in values.split(",") if int(x)%2!=0]
# print(",".join(numbers))

# netAmount=0
# while True:
#     s=input()
#     if not s:
#         break
#     values=s.split(" ")
#     operation=values[0]
#     amount=int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
#     print(netAmount)
#         continue
#     elif re.search("\s",p):

# import re
# value=[]
# items=[x for x in input().split(',')]
# for p in items:
#      if len(p)<6 or len(p)>12:
#          continue
#      else:
#          pass
#      if not re.search("[a-z]",p):
#          continue
#      elif not re.search("[0-9]",p):
#          continue
#      elif not re.search("[A-Z]",p):
#          continue
#      elif not re.search("[$#@]",p):   continue
#      else:
#          pass
#      value.append(p)
# print(",".join(value))

### l=[]
# while True:
#     s=input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
# print(sorted(l,key=itemgetter(0,1,2)))

# def putNumbers(n):
#     i=0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# for i in reverse(100):
#   print(i)

# import math
# pos=[0,0]
# while True:
#     s=input()
#     if not s:
#         break
#     movement=s.split(" ")
#     direction=movement[0]
#     steps=int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

### freq={ }
# line=input()
# for word in line.split():
#     freq[word]=freq.get(word,0)+1
# words=freq.keys()
# word.sort()
# for w in words:
#     print("%s:%d"%(w,freq[w]))

# def square(num):
#     return num**2
# print(square(2))
# print(square(3))

# print (abs.__doc__)
# print (int.__doc__)
# print (input.__doc__)
# def square(num):
#     ''' Return the square value of the input number.
#     The input number must be integer.
#     '''
#     return num**2
# print(square(2))
# print(square.__doc__)

### class Person:
#     # Define the class parameter"name"
#     name="Person"
#     def__init__(self,name=None):
#         # self.name is the instance parameter
#         self.name=name
# jeffrey=Person("Jeffrey")
# print("%s name is %s"%(Person.name,jeffrey.name))
# nico=Person()
# nico.name="Nico"
# print("%s name is %s"%(Person.name,nico.name))

# def sumFunction(number1,number2):
#     return number1+number2
# print(sumFunction(1,2))

# def printValue(n):
#     print (str(n))
# printValue(3)

# def printValue(n):
#     print (str(n))
# printValue(3)

# def printValue(s1,s2):
#     print (int(s1)+int(s2))
# printValue("3","4")  #7

# def printValue(s1,s2):
#     print (s1+s2)
# printValue("3","4")   #34

# def printValue(s1,s2):
#     len1=len(s1)
#     len2=len(s2)
#     if len1>len2:
#         print (s1)
#     elif len2>len1:
#         print(s2)
#     else:
#         print (s1)
#         print (s2)
# printValue("one","three")

# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         c=a
#         a=b
#         b=c+b
# fib(10)

# s='my name is siva'
# n=''
# for i in s:
#     n=i+n
# # print(n)
# p=" "
# for j in n.split(" "):
#     p=p+" "+j
# print(p)

# def checkvalue(n):
#     if n%2==0:
#            print("it is an even number")
#     else:
#            print("it is an odd number")
# checkvalue(7)

# def printdict():
#          d=dict()
#          d[1]=1
#          d[2]=2**2
#          d[3]=3**2
#          print(d)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#            d[i]=i**2
#     print(d)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#             d[i]=i**2
#     for(k,v) in d.items():
#             print(v)
# printdict()

# def printdict():
#     d=dict()
#     for i in range(1,21):
#              d[i]=i**2
#     for k in d.keys():
#              print(k)
# printdict()

# def printlist():
#     li=list()
#     for i in range(1,21):
#             li.append(i**2)
#     print(li)
# printlist()

# def printlist():
#     li=list()
#     li.append(i**2)
#     print (li[:5])

# def printlist():
#     li=list()
#     for i in range(1,21):
#             li.append(i**2)
#     print (li[-5:])
# printlist()

# def printlist():
#     li=list()
#     for i in range(1,21):
#             li.append(i**2)
#     print(li[5:])
# printlist()

# def printtuple():
#     li=list()
#     for i in range(1,21):
#            li.append(i**2)
#     print(tuple(li))
# printtuple()

# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)

 # li=list()
 # for i in tp:
 #     if tp[i]%2==0:
 #              li.append(tp[i])
 #     tp2=tuple(li)
 # print(tp2)

# s=input()
# if s=="yes" or s=="YES" or s=="Yes":
#     print("Yes")
# else:
#     print("No")

# li=[1,2,3,4,5,6,7,8,9,10]
# evennumbers=filter(lambda x:x%2==0,li)
# print(evennumbers)

# li=[1,2,3,4,5,6,7,8,9,10]
# squarenumbers=map(lambda x:x**2,li)
# print(squarenumbers)

# li=[1,2,3,4,5,6,7,8,9,10]
# evennumbers=map(lambda x:x**2,filter(lambda x:x%2==0,li))
# print(evennumbers)

# evennumbers=filter(lambda x:x%2==0, range(1,21))
# print(evennumbers)

# print(squarenumber)

# #class American(object):
#       def printNationlity():
#           print("America")
# anAmerican=American()
# anAmerican.printNationality()
# American.printNationality()

# class American(object):
#     pass
# class NewYorker(American):
#     pass
# anAmerican=American()
# aNewYorker=NewYorker()
# print(anAmerican)
# print(aNewYorker)

# class circle(object):
#     def__init__(self, r):
#     self.radius=re
#     def area(self):
#          return self.radius**2*3.14
# acircle=circle(2)
# print(acircle.area())

# class Circle(object):
#     def __init__(self, r):
#       self.radius=r
#     def area (self):
#         return self.radius**2*3.14
# aCircle= Circle(2)
# print (aCircle.area())

# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
# aRectangle=Rectangle(2,10)
# print(aRectangle.area())

# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l
#     def area(self):
#         return self.length*self.length
# aSquare= Square(3)
# print(aSquare.area())

# def throws ():
#     return 5/0
# try:
#     throws()
# except ZeroDivisionError:
#     print ("division by zero!")
# except ExceptionError:
#     print ('Caught an exception')
# finally:
#     print ('In finally block for cleanup')

"""My own exception class
 Attributes:
      msg --explanation of the error
 """
# def __init__(self,msg):
#     self.msg = msg
# error = MyError("something wrong")

# import re
# emailAddress=input()
# pat2="(\w+)@((\w+\.)+(com))"
# r2=re.match(pat2,emailAddress)
# print(r2.group(1))

# import re
# emailAddress = input()
# pat2 = "(\w+)@(\w+)\.(com)"
# r2 = re.match(pat2,emailAddress)
# print(r2.group(2))

# import re
# s=input()
# print(re.findall("\d+",s))

# unicodeString = u"hello world!"

# s=input()
# u=unicode( s,"utf-8")
# print(u)

# -*- coding: utf-8 -*-

# n=int(input())
# sum=0.0
# for i in range(1,n+1):
#     sum +=float(float(i))/(i+1)
# print(sum)

# def f(n):
#     if n==0:
#         return 0
#     return f(n-1)+100
# n=int(input())
# print(f(n))

# def f(n):
#     if n== 0:return 0
#     elif n==1: return 1
#     else: return f(n-1)+f(n-2)
# n=int (input())
# print (f(n))

# def f(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else: return f(n-1)+(n-2)
# n=int(input())
# values=[str(f(x)) for x in range(0, n+1)]
# print (",".join (values))

# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1
# n=int (input())
# values=[]
# for i in EvenGenerator(n):
#     values.append (str(i))
# print (",".join(values))

# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input())
# values=[]
# for i in NumGenerator(n):
#     values.append(str(i))
# print(",".join(values))

# li=[2,4,6,8]
# for i in li:
#     assert i%2==0

# expression=input()
# print(eval(expression))

# import math
# def bin_search(li, element):
#     bottom=0
#     top=len(li)-1
#     index=-1
#     while top>=bottom and index==-1:
#      mid = int(math.floor((top+bottom)/2.0))
#     if li[mid]==element:
#         index=mid
#     elif li[mid]>element:
#         top=mid-1
#     else:
#         bottom=mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))

# import math
# def bin_search(li,element):
#     bottom=0
#     top=len(li)-1
#     index=-1
#     while top>=bottom and index==-1:
#         mid=int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index=mid
#         elif li[mid]>element:
#             top=mid-1
#         else:
#             bottom=mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))

# import random
# print (random.random()*100)

# import random
# print (random.random()*100-5)

# import  random
# print(random.choice([i for i in range(11) if i%2==0]))

# import random
# print (random.choice([i for i in range (201)if i%5==0 and i%7==0]))

# import random

# import random
# print (random.sample([i for i in range(100,201) if i%2==0],5))

# import random
# print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))

# import random
# print(random.randrange(7,16))

# import zlib
# s='hello world!hello world!hello world!hello world!'
# t= zlib.compress(s)
# print(t)
# print(zlib.decompress(t))

# from timeit import Timer
# t=Timer("for i in range(100):1+1")
# print(t.timeit())

# from random import shuffle
# li=[3,6,7,8]
# shuffle(li)
# print(li)

# from random import shuffle
# li=[3,6,7,8]
# shuffle(li)
# print(li)

# subjects=["I","You"]
# verbs=["Plays","Love"]
# objects=["Hockey","Football"]
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence="%s %s %s." %(subjects[i],verbs[j],objects[k])
#             print(sentence)

# li=[5,6,77,45,22,12,24]
# li=[x for x in li if x%2!=0]
# print(li)

# li=[12,24,35,70,88,120,155]
# li=[x for x in li if x%5!=0 and x%7!=0]
# print(li)

# li=[12,24,35,70,88,120,155]
# li=[x for (i,x) in enumerate(li) if i%2!=0]
# print(li)

# array=[[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)

# li=[12,24,35,70,88,120,155]
# li=[x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print(li)

# li=[12,24,35,70,88,120,155]
# li=[x for x in li if x!=24]
# print(li)

# set1=set([1,3,6,78,35,55])
# set2=set([12,24,35,24,88,120,155])
# set1&=set2
# print(1,2)

# def removeDuplicate(li):
#     newli=[]
#     seen=set()
#     for item in li:
#         if item not in seen:
#             seen.add(item)
#             newli.append(item)
#     return newli
# li=[12,24,35,24,88,120,155,88,120,155]
# print(removeDuplicate(li))

# class Person(object):
#     def getGender(self):
#         return"Unknown"
# class Male(Person):
#     def getGender(self):
#         return"Male"
# class Female(Person):
#     def getGender(self):
#         return"Female"
# aMale=Male()
# aFemale=Female()
# print(aMale.getGender())
# print(aFemale.getGender())

# dic={}
# s=input()
# dic[s]=dic.get(s,0)+1
# print('\n'.join(['%s,%s'%(k,v) for k,v in dic.items()]))

# s=input()
# s=s[::-1]
# print (s)

# s=input ()
# s=s[::2]
# print (s)

# def solve(numheads,numlegs):
#     ns='No soluntions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
# numheads=35
# numlegs=94
# solutions=solve(numheads,numlegs)
# print(solutions)

# l=[]
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#         pri lnt(','.join(l))

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#     print(d)


# #!/usforr/bin/env python
# import math
# c=50
# h=30
# value=[]
# items=[x for x in input().split(',')]
# for d in items:
#     value.append (str(round(math.sqrt(2*c*float(d)/h))))
#     print(','.join(value))


# inpu_str=input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist=[[0 for col in rage(colNum)]for row in range(rowNum)]
# for col in range(colNum):
#     multilist[row][col]=row*col
#     print(multilist)

# lines=[]
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#         for sentence in lines:
#             print(sentence)
#
# values=input()
# l=values.split
# t=tuple(1)
# print(1)
# print(t)

# s=input()
# d={"DIGITS":0,"LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
#     print("LETTERS",d["LETTERS"])
#     print("DIGITS",d["DIGITS"])

# s=input()
# d={"UPPER CASE":0  "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPRE CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
#     print("UPPER CASE",d["UPPER CASE"])
#     print("LOWER CASE",d["LOWER CADSE"])
    



# 82077623724


# int=10
# print(int)

# a=10
# b=20
# print(a,b)

# a=10
# b=15
# print(a)
# print(b)

# a=5
# b=2
# print(a+b)

# for i in range(10):
#     while i<=5:
#         if i==5:
#             pass
#         print(i)
#

num











































































































































































