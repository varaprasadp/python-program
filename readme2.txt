I have done thos using set operations so i have converted lists to sets
L1=set(L1)
L2=set(L2)

to find common elements i used set operation &

comm_elements=list(L1&L2)

this line checks if any list is empty or not and if common elments list is empty
if len(L1)==0 or len(L2)==0 or len(common_elements)==0

otherwise it prints the common elements


to find elements present in L1 and not in L2 i used '-' set operation
