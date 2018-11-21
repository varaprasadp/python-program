import os,sys
#input directory
a=input()#"/Users/vara1/Desktop/gate/"
#fuction for recursion to print sub directories
def proff(a):
    p=a
    for name in os.listdir(p):
        #if it is a file we will print here
        if os.path.isfile(p+name):
            print(name)
        #if it is directory we will call the function for printing paths of sub-directory    
        elif os.path.isdir(p+name):
            proff(p+name+"/")
#calling function            
proff(a)
        
