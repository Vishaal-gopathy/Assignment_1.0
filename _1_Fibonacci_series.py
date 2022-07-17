


limit = int(input("Enter the end term: "))
n1 , n2 = 0,1

print("the fibonacci series is : ")
while n1 < limit:
    print(n1, end = " ")
    n= n1 + n2    
    n1 = n2 
    n2 = n
    
    
