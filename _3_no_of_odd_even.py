Start = int(input("Enter the start value : "))
End = int(input("Enter the end value : "))

odd_no , even_no = 0,0
for i in range(Start,End+1):
    if i % 2!= 0:
        odd_no +=1
    else:
        even_no +=1
print ("total number of odd numbers : ",odd_no)
print("total number of even numbers : ",even_no)            
