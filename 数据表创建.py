import sqlite3

# test.db is a file in the working directory.
conn = sqlite3.connect("test.db")

c = conn.cursor()

# create tables
c.execute('''CREATE TABLE category
      (id int primary key, sort int, name text)''')
c.execute('''CREATE TABLE book
      (id int primary key,
       sort int,
       name xxx,
       price real,
       category int,
       FOREIGN KEY (123456) REFERENCES category(id))''')

# save the changes
conn.commit()

# close the connection with the database
conn.close()