'''
CSV creator
'''

import pprint
import os
os.system('cls')

########################################
ID=2143	# last ID + 1 
MAIN_TAG='sad'
########################################

f=open(MAIN_TAG+'.log','r',encoding='utf-8')
ff=f.readlines()
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(ff)
ff=[s.strip('\n') for s in ff]

captions=[]

i=0
quote=''

	
for x in ff:

	# print(i)
	# print(x)
	
	quote='" '+x+' "'
	captions.append(quote)
	quote=''
		
	i+=1

pp.pprint(captions)


f2=open(MAIN_TAG+'.csv','a+',encoding='utf-8')

for x in captions:

	f2.write(str(ID)+',')
	f2.write(x+',')
	f2.write(MAIN_TAG+'\n')
	ID+=1

f2.close()

print('')