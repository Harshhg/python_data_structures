def num_ways(n,mem):
     if(mem[n] is not None):
          return mem[n]
     if(n==0 or n==1):
          return 1
     mem[n] = num_ways(n-1,mem)+num_ways(n-2,mem)
     return mem[n]

n=int(input())
mem=[None] * (n+1)
print(num_ways(n,mem))
