char = input("Enter the word you want to reverse : ")
rev_char = ""

for word in char:
    rev_char = word + rev_char
    
print("the original word is : ",char)
print("the reversed word is : ",rev_char)    
