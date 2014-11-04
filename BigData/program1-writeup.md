From the given four formats I choose SQL to convert into a json.

How ?

I would like to convert the SQL file to Json file using PHP. And that can be done using the following lines of code

```$stmt = $dbh->query("SELECT * FROM " . $table);```
   
```$data = $stmt->fetchAll(PDO::FETCH_ASSOC);```

```echo json_encode($data);```

Why ?

--> The reason am using PHP is because of its flexibility and its built-in database support.

--> And the reason why am choosing SQL out of the four formats is that, all four files contains the same set of GPS points and SQL has the least memory size. Although XML compresses best it has the largest size than all others. It comes to the almost same size as others does.

Comparison:-

When I tried to compress these files using the ZIP and GZIP mechanisms I got the same results as shown in the below table. But XML is the one which got compressed most and then YML. SQL and CSV are almost compressed to similar extent, where CSV is just a bit more than the SQL.


| Format        | Original Size | Zip  | Gzip | Percentage   |
| ------------- |:-------------:|:----:|:----:|:------------:|
| CSV           |  84 MB        | 59 MB|59 MB |	    87.9%    | 
| SQL           |  467 MB       | 60 MB|60 MB |	    87.3%    | 
| XML           |  2.3 GB       | 75 MB|75 MB |	    96.7%    | 
| YML           |  771 MB       | 61 MB|61 MB |	    92.1%    | 

