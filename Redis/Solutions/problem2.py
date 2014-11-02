import redis
import sys
import json
import string

def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True

#opening the file to be read	
file=open('../nutrition.json','r')

#linking up with redis
red_access=redis.StrictRedis(host='localhost',port=6379,db=0)

#checking each line in the input file whether it is valid json or not
for line in file:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		#if that is valid line add the corresponding nutrients array for respective line to nutrients array
		nutrients=line['nutrients']
		
		#adding all the fields of nutrients into a set which allows the unique entries
		for nut in nutrients:
			red_access.sadd("Nut_List",nut['_id'])

#finally print the Unique number of nutrients present in the total json file
print "Unique Number of Nutrients: "			
print red_access.scard("Nut_List")