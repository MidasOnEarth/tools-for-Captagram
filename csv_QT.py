'''
CSV creator
'''

import pprint
import os
os.system('cls')

########################################
ID=1008	# last ID + 1 
MAIN_TAG='life'
########################################

f=open(MAIN_TAG+'.log','r')
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
	
	if(i%2==0):
		quote+='" '+x + ' "'
	if(i%2==1):
		captions.append(quote)
		quote=''
		
	i+=1

pp.pprint(captions)





f2=open(MAIN_TAG+'.csv','a+')

for x in captions:

	f2.write(str(ID)+',')
	f2.write(x+',')
	f2.write(MAIN_TAG+'\n')
	ID+=1

f2.close()

print('')