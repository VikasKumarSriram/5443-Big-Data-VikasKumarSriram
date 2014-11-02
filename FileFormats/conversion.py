import csv, json

csvfile = open('GpsFilePoints.csv.1', 'r')
jsonfile = open('sample.json', 'w')

fieldnames = ("word1","freq1", "word2","freq2")
reader = csv.reader(csvfile, fieldnames)

out = json.dumps( [ dict(zip(row[::2], row[1::2])) for row in reader ] )
jsonfile.write(out)