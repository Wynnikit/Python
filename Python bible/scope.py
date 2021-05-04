# 2 types of scope: local and global
#python functions create local scopes, but not loops or if statements


#a = 250    # global scope variable

#def f1():
 #   b = a +10
   # print(b)                        #global variables cannot be overwritten inside a fuction w/ local variables

#def f1():
   # global a                           #global keyword can overwrite outside global variable
    #a = 100
    #print(a)

#def f2():
 #   a = 50                       #local variable will be used within confines of the function
  #  print(a)

#f1()
#f2()
    
#print(a)



a = [1,2,3]

def f1():
    a[0] = 5                    #a small piece of a list/dictionary can be overwritten
    print(a)

def f2():
    a = 50                      
    print(a)


f1()
f2()
print(a)



