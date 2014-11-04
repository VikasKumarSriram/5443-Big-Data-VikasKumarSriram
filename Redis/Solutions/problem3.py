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

		for nutrient in line['nutrients']:
			red_access.zincrby('count',nutrient['tagname'],1)

#storing the Top 5 occurring nutrients into a list
result=red_access.zrevrange('count',0,5,withscores=True)

#Printing the Top 5 occurring nutrients
for nut in result:
	print nut[0]
	print " occurs "
	print red_access.zscore('count',nut[0])
	print " times "
