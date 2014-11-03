__Problem 1)__
 
  What are the number of unique food "items" in the file. You might be tempted to count the number of lines, since we assume that each line contains one food item. I will warn you that this is an incorrect solution. Just by chance, there might be a few duplicated rows in the file, therefore line counting would be wrong.

__Solution:__ 
  
  In my solution to get the number of unique "food items" in the file firstly I used 'sadd' command of redis to store the entries of the feild " _id". As set accepts only one entry of a perticular element I added them into a set. Further to display the number of food items I used 'scard' command which prints the length of set.
  
  Output: 
   Unique food items:
   8194
  
__Problem 2)__
 
 How many unique nutrients are there?

__Solution__
  
  In my solution to get the number of unique nutrients in the file I added the entries of "_id " feild in nutrient array to a set using the redis command 'sadd'. There after to print the number of unique lines I used 'scard' command of redis which prints the length of the previous set mentioned.
  
  Output:
   Unique Number of Nutrients:
   146
   
__Problem 3)__
  
  What are the top 5 most commonly occuring nutrients?
  
__Solution:__

  In my solution to print the most commonly occuring nutrients firstly I used 'zincrby' command of redis which stores the each element of list along with the some value. All the elements are stored in sorted order. In this program, I gave the value of the each elemnt as the number of occurances by using for loop. There after by using the 'zrevrange' command I stored the top 5 frequently occured elemnts into a new list called result and finally I printed them.
  
  Output:
   

__Problem 4)__
 
  Given a specific nutrient, what percentage of food items contain this nutrient?
  
__Solution:__
 
  In my solution to keep track of a perticular nutrient i.e., how many times it is repeated for different food items I used 'zincrby' command of redis. Then I stored the length of the food items list using 'zscore' command of redis and to know the total food items in the input I used 'score' command of redis. To print the percentage of food items with perticular nutrient say 'FIBTG' I divided the food items with this nutrient with the total number of nutrients and multiplied it by 100. And hence got my result.
 Output:
  '' occurs 10270.0 times 
  VITD occurs 9524.0 times 
  PROCNT occurs 8194.0 times
  ENERC_KCAL occurs 8194.0 times
  CHOCDF occurs 8194.0 times 
  
__Problem 5)__
  This problem is more about size of the database depending on how data is stored. I want the size of the data base on disk (remember info && human readable). You will also need to make sure you run flushall before loading this structure.You can make multiple passes on the data, and I'm not looking for extremely efficient processing, I just want it loaded as prescribed. You don't have to perform tasks in the order asked either. I just want to final resulting data structures, and size of all of them on disk.

  -Store all id's for nutrients in a set.
  -Store all nutrients in a hash with thier id's as keys.
  -Store all tagnames in a set.
  -Store all nutrients in a hash with tagnames as keys.
  -Store all nutrient id's in a list with the item id (top level _id) as the key.

__Solution:__

  In my solution,to store 
   all id's to a set I used 'sadd' command.
   all id's to hash set I used 'hset' command.
   all tagnames to set I used 'sadd' command.
   all tagnames to hash list IO used 'hset' command.
  
