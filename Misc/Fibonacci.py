__author__ = 'shearora'

### Fibonacci sequence without recursion

def fib(n): # n is number of elements in the sequence
    first = 0
    second = 1
    item =0
    if(n >= 1):
        print (first)
        item += 1
    if(n >= 2):
        print (second)
        item += 1

    while (item < n):
        val = first + second
        print (val)
        first = second
        second = val
        item += 1


def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))





