# Given an integer, n, and  space-separated integers as input, create a tuple, n, of those  integers. 
# Then compute and print the result of hash(t).


n = int(input()) 
  
a = list(map(int,input().strip().split()))[:n] 

a = tuple(a)
  
outputHash = hash(a)

print(outputHash)