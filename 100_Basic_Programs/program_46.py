# 46.  Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10].

l=[1,2,3,4,5,6,7,8,9,10]
sqreven=list((map(lambda x:x**2, filter(lambda a:a%2==0, l))))
print(sqreven)