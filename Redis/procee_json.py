import redis
import string
import json
import sys

def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

   
#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)

f = open('./nutrition.json','r')
f1 = open("nclean.json", "w")
f3 = open("Writeup.md", "w")
 
# Read one line from file

valid_linecount=0
invalid_linecount=0
total_linecount=0
ratio=0

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	total_linecount = total_linecount + 1
	
	if is_json(line):
			valid_linecount = valid_linecount + 1
			line = json.loads(filter(lambda x: x in string.printable, line))
			f1.write(str(line))
	else : 
			invalid_linecount = invalid_linecount + 1

ratio = valid_linecount/invalid_linecount
			
f3.write('### Json File Processing\n')	
f3.write('Total lines '+str(total_linecount))
f3.write('\n Valid lines '+str(valid_linecount))		
f3.write('\n Invalid lines '+str(invalid_linecount))
f3.write('\n Ratio to Good to Bad line '+str(ratio))

f.close()
f1.close()
f3.close()