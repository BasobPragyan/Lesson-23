#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
mydict_code={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977','United Kingdom':'44'}
print("Country code for India",mydict_code.get('India','Not found'))
print("Country code for U.S",mydict_code.get('U.S','Not found'))
print("Country code for U,K",mydict_code.get('United Kingdom','Not found'))