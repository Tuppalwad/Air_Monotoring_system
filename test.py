#positive and negative number find 
from linecache import getline
from locale import getpreferredencoding
from traceback import print_tb


def get_positive_and_negative(n):
    if n<0:
        print("Negative")
    elif n>0:
        print("Positive number")

#even and odd number in python
def enven_and_odd(n):
    if n%2==0:
        print('Number is Even')
    else:
        print("Number is odd")
        
#sum of first n natural numbers 

def sum_of_natural_number(range):
    i=range
    ans=0 
    while i>0:
        ans+=i 
        i-=1 
        
    print(ans)
#greatest of two number
def greates_of_two_number(a,b):
    if a>b:
        print("a is greates ")
    else:
        print('b is greatest')
#swap number without using third variable
def swap(a,b):
    print(f'{a} a is and {b} b is ')
    a=a+b 
    b=a-b 
    a=a-b 
    print(a,b)
# swap(3,4)

#leap year or not 
def get_leap_year(year):
    if (year%4==0 and  year %100!=0 ) or year%400==0:
        print('leap year ')
    else:
        print('Not leap year ')
# get_leap_year(2022)
#prime number 
def get_prime_Nuber(a,b):#prime number from range a to b 
    l=[]
    i=a 
    while i<=b:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
        i+=1
    print(l)
# get_prime_Nuber(11,23)

#get gcd of two number
import math 
def get_gcd(a,b):
    print('hi')
    print(math.gcd(a,b))
# get_gcd(5,5)

def get_gcd(a,b):
    print('hi')
    print(math.lcm(a,b))
# get_gcd(5,5)

#get count of element in array 
def get_cout(a):
    d={}
    for i in a:
        d[i]=a.count(i)
    ans=0
    for i,j in d.items():
        if j>1:
            ans+=math.factorial(j)/((math.factorial(j-2))*math.factorial(2))
    print(int(ans))
# get_cout([2,5,5,2,9,9,9,12])

#get_count by dictonary

def get_count_by_dict(l):
    ans={}
    for i in l:
        if i in ans:
            ans[i]=+1
        else:
            ans[i]=1
    print(ans)
    
#find number of van if you have ginven a no of tiers
def get_van(v,n):
    car=0 
    van=0 
    for i in range(v):
        x=v-i 
        if 2*x + 4*i==n:
            car=x
            van=i 
            break
    print(car,van)
get_van(100,200)