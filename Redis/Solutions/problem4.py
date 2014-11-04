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

	
Food_Item = 'FIBTG'

#opening the file to be read	
file=open('../nutrition.json','r')

#linking up with redis
red_access=redis.StrictRedis(host='localhost',port=6379,db=0)
red_access.flushdb()

#checking each line in the input file whether it is valid json or not
for line in file:
	line = json.loads(filter(lambda x: x in string.printable, line))
	
	#if this is valid keep a record of the count of food items
	for FoodItmVal in line['nutrients']:
		red_access.zincrby('count',FoodItmVal['tagname'],1)
	red_access.sadd('lines',line['_id'])

Total_lines=red_access.scard('lines')
Food_Item_count=red_access.zscore('count',Food_Item)
x = float(Food_Itam_count)*100/float(Total_lines)
print ("Total number of occurrences of ",Food_Item," is ",Food_Item_count)
print ("Total number of lines is",Total_lines)
<<<<<<< HEAD
print (Food_Item," occurs in ",x,"% of food items")
=======
print (Food_Item," occurs in ",x,"% of food items")
>>>>>>> 33aa5602ad2bcd1632a315ba855e5b0a43ebe85b
