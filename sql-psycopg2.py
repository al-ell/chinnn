import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database 
cursor = connection.cursor()

# query 1 - select all records from "artist" table
# cursor.execute('SELECT * FROM "artist"')


# query 3 - only queen from artist table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# query 4 - only queen from artist table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# query 5 - albums with id 51 from album table 
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# query 6 - only queen tracks from track table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetch the results (multiple)
# results = cursor.fetchall()

# fetch the result (single)
results = cursor.fetchone()

# close the connecton
connection.close()

# print results
for result in results:
    print(result)

