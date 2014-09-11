From the given four formats I choose SQL to convert into a json.

How ?
I would like to convert the SQL file to Json file using PHP. And that can be done using the following lines of code

```$stmt = $dbh->query("SELECT * FROM " . $table);```
$data = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($data);

Why ?
--> The reason am using PHP is because of its flexibility and its built-in database support.
--> And the reason why am choosing SQL out of the four formats is that, all four files contains the same set of GPS points and SQL has the least memory size. Although XML compresses best it has the largest size than all others. It comes to the almost same size as others does.
Comparison
