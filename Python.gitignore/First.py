#QUESTION NO.1
print('MENU'.center(20))

item=['stick','cone','cup','chocolate','vanila','strawberry']
rupees=[1,2,3,4,5,6]

print('ICE CREAM TYPE:')
for i in range(len(item)):
    if i==(len(item)//2): #floure start here
        print('FLOURE:')
    print(item[i].center(20),rupees[i])
print()

#QUESTION NO.2
print('CAST OF EACH ICE'.center(20))

#ice and cost dictionary
ice_type_dic={'stick':1,'cone':2,'cup':3,}
floure_dic={'chocolate':4,'vanila':5,'strawberry':6}

for j in ice_type_dic:
    for k in floure_dic:
        print((j+' '+k).center(20),ice_type_dic[j]+floure_dic[k]) #ice combination
print()

#QUESTION NO.3
print('SELECT YOUR FAVOUR'.center(20))

no_item,floure,ice_type=map(str,input().split(' ')) #input from user
print(int(no_item)*(floure_dic[floure]+ice_type_dic[ice_type]))
