#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
mydict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
k=2
result=0
for key in mydict:
    if mydict[key]==k:
        result=result+1
print("Dictionary is",mydict)
print("Frequency is: ",result)