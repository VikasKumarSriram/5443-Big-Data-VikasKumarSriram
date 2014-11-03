#Problem 1)
  What are the number of unique food "items" in the file. You might be tempted to count the number of lines, since we assume that each line contains one food item. I will warn you that this is an incorrect solution. Just by chance, there might be a few duplicated rows in the file, therefore line counting would be wrong.

#Solution: 
  In my solution to get the number of unique "food items" in the file firstly I used 'sadd' command of redis to store the entries of the feild " _id". As set accepts only one entry of a perticular element I added them into a set. Further to display the number of food items I used 'scard' command which prints the length of set.
  
#Problem 2)
 How many unique nutrients are there?

#Solution:
  In my solution to get the number of unique nutrients in the file I added the "_id "
#Problem 3)
  What are the top 5 most commonly occuring nutrient?
  
#Problem 4)
  Given a specific nutrient, what percentage of food items contain this nutrient?
  
#Problem 5)
  This problem is more about size of the database depending on how data is stored. I want the size of the data base on disk (remember info && human readable). You will also need to make sure you run flushall before loading this structure.You can make multiple passes on the data, and I'm not looking for extremely efficient processing, I just want it loaded as prescribed. You don't have to perform tasks in the order asked either. I just want to final resulting data structures, and size of all of them on disk.

  -Store all id's for nutrients in a set.
  -Store all nutrients in a hash with thier id's as keys.
  -Store all tagnames in a set.
  -Store all nutrients in a hash with tagnames as keys.
  -Store all nutrient id's in a list with the item id (top level _id) as the key.
