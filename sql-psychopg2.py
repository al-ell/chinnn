import psychopg2

# connect to "chinook" database
connection = psychopg2.connect(database="chinook")

# build a cursor object of the database 
cursor = connection.cursor()

# query 1 - select all records from "artist" table
cursor.execute('SELECT * FROM "artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connecton
connection.close()

# print results
for result in results:
    print(result)

