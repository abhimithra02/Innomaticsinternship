A=int(input())
Store=set(input().split());
B=int(input())
Store2=set(input().split());
Store3=Store.union(Store2)
print(len(Store3))
