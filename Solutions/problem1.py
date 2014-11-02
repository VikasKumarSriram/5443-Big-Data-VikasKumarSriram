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
red_access.flushdb()

#checking each line in the input file whether it is valid json or not
for line in file:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		#if that is valid line add it to the set, which allows the unique entry of the elements.
		#even if we get the duplicate entries set ignores them
		red_access.sadd("unique_food_items",line['_id'])
		
#finally the unique number is known by printing the length of the set 	

print "Unique Food Items:"	
print red_access.scard("unique_food_items")