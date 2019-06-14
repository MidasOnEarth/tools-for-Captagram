# import requests
# import pprint

# api_key = 'acc_47dc4fefe85582e'
# api_secret = '197c9635dddb4198514c3eac8c82d7dd'
# image_url = 'https://cdn.pixabay.com/photo/2014/12/17/21/30/wild-flowers-571940_960_720.jpg'

# response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url,auth=(api_key, api_secret))

# print( response.json())


'''
# ========================================================================================================================
# ========================================================================================================================
# save photo details to files
'''

# import requests

# api_key = 'acc_47dc4fefe85582e'
# api_secret = '197c9635dddb4198514c3eac8c82d7dd'

# def retImgInfo(img):
	# image_path = img+'.jpeg'
	# response = requests.post('https://api.imagga.com/v2/tags',
	# auth=(api_key, api_secret),
	# files={'image': open(image_path, 'rb')})
	# return response.json()

# imgs=['ee1']

# for x in imgs:
	# z=retImgInfo(x)
	# f=open(x+'.txt','w+')
	# f.write(str(z))
	# f.close()
	# print('done with ',x)

'''
# ========================================================================================================================
# ========================================================================================================================
# extract tags from photo directly
'''

import requests

api_key = 'acc_47dc4fefe85582e'
api_secret = '197c9635dddb4198514c3eac8c82d7dd'

image_path = 'e2.jpg'
response = requests.post('https://api.imagga.com/v2/tags',
auth=(api_key, api_secret),
files={'image': open(image_path, 'rb')})

x=response.json()
tags=[]

ctr=0
for i in x['result']['tags']:
	zz=list(x['result']['tags'][ctr]['tag'].values())
	tags.append(zz)
	ctr+=1
	if(ctr>20):
		break
		
t1=[]

for x in tags:
	for i in x:
		t1.append(i)
		
print(t1)

q='happy'
op=q in t1
print(q,' in photo: ',op)
