'''python program to find common elements and elements present in L1 and not in L2
 where L1 ,L2 are two lists given'''
#Taking input

print("enter elements of the list L1 with spaces")
L1=input().split()

print("enter the elements of the list L2 with spaces")
L2=input().split()

#for set operations convert lists to sets

L1=set(L1)
L2=set(L2)

#finding common elements

comm_elements=list(L1&L2)

if len(L1)==0 or len(L2)==0 or len(common_elements)==0:
    print("there are no common elements")
else:    
    print("common elements of L1 and L2: ",comm_elements)

#finding elements present in L1 and not in L2

m=list(L1-L2)
if len(m)==0:
    print("all elements in L2 are present in L1 OR L1 is empty!")
else:
    print("elements present in L1 and not in L2: ",m)
