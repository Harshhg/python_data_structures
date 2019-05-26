def fib(n,arr):
     if(arr[n] is not None):
          return arr[n]         //fetching the computed value
     if(n==1 or n==2):
        return 1
     else:
          arr[n] = fib(n-1,arr) + fib(n-2,arr)    //storing the computed value so that need not to compute again

     return arr[n]

def fibarr(n):
     arr = [None] * (n+1)     //initializing list with null values
     return fib(n,arr)

print(fibarr(50))
