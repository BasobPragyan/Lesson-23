mydict={'id1':
        {'Name':'Pragyan',
         'class':9,
         'sub':'Science,Maths,SSC,AI'},
        'id2':
         {'Name':'Basob',
          'class':8,
          'sub':'Maths,Science,music'},
           'id3':
            {'Name':'Pragyan',
         'class':9,
         'sub':'Science,Maths,SSC,AI'},
          'id4':
           {'Name':'Basob',
          'class':8,
          'sub':'Maths,Science,music'} }
result={}
for key,value in mydict.items():
    if value not in result.values():
        result[key]=value
print("Original dictionary is : ",mydict)
print("Updated dictionary is : ",result)