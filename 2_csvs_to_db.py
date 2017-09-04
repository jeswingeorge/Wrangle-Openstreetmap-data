import sqlite3
import csv
from pprint import pprint

# Connect to the database (if it doesn't exist, it will be created in the folder that your notebook is in):
sqlite_file = 'delhi.db'    # name of the sqlite database file

# Connect to the database
conn = sqlite3.connect(sqlite_file)

# Get a cursor object
cur = conn.cursor()

# Create the table nodes

# Create the table nodes, specifying the column names and data types:
cur.execute(''' CREATE TABLE nodes(id INTEGER, lat INTEGER, lon INTEGER, user TEXT, uid INTEGER, version INTEGER, changeset TEXT,
timestamp TEXT)
''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"), i['lat'].decode("utf-8"), i['lon'].decode("utf-8"), i['user'].decode("utf-8"),
             i['uid'].decode("utf-8"), i['version'].decode("utf-8"), i['changeset'].decode("utf-8"), 
              i['timestamp'].decode("utf-8")) 
               
             for i in dr]
    
# insert the formatted data
cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", 
                to_db)
# commit the changes
conn.commit()


# Create the table nodes_tags

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE nodes_tags(id INTEGER, key INTEGER, value TEXT, type TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('nodes_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"), i['key'].decode("utf-8"), i['value'].decode("utf-8"), i['type'].decode("utf-8")) 
               for i in dr]
    
# insert the formatted data
cur.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()


# Create the table ways

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways(id INTEGER, user TEXT, uid INTEGER, version INTEGER, changeset TEXT,
timestamp TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"), i['user'].decode("utf-8"), i['uid'].decode("utf-8"), i['version'].decode("utf-8"),
             i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) 
               for i in dr]

    
# insert the formatted data
cur.executemany("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()


# Create the table ways_nodes

# Create the table.
#Before you (re)create the table, you will have to drop the table if it already exists: 

cur.execute('''DROP TABLE IF EXISTS ways_nodes''')
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways_nodes(id INTEGER, node_id INTEGER, position INTEGER) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways_nodes.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"), i['node_id'].decode("utf-8"), i['position'].decode("utf-8")) 
               for i in dr]

# insert the formatted data
cur.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)
# commit the changes
conn.commit()




# Create the table ways_tags


# Create the table.
#Before you (re)create the table, you will have to drop the table if it already exists: 

cur.execute('''DROP TABLE IF EXISTS ways_tags''')
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways_tags(id INTEGER, key INTEGER, value TEXT, type TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways_tags.csv','rb') as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'].decode("utf-8"), i['key'].decode("utf-8"), i['value'].decode("utf-8"), i['type'].decode("utf-8")) 
               for i in dr]

    
    
# insert the formatted data
cur.executemany("INSERT INTO ways_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()






# close the connection:
conn.close()
























