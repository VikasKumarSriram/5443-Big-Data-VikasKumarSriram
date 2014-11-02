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
file=open('/var/www/html/5443-Big-Data-VikasKumarSriram/BigData/Redis/nutrition.json','r')

#linking up with redis
red_access=redis.StrictRedis(host='localhost',port=6379,db=0)
red_access.flushdb()

#checking each line in the input file whether it is valid json or not
for line in file:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		
		for nut  in line['nutrients']:
			red_access.sadd("id_set",nut['_id'])
			red_access.hset("id_hash",nut['_id'],nut['tagname'])
			red_access.sadd("TagName_set",nut['tagname'])
			red_access.hset("TagName_hash",nut['tagname'],nut)
			
print red_access.smembers("id_set")
print red_access.hgetall("id_hash")
print red_access.smembers("TagName_set")
print red_access.hgetall("TagName_hash")