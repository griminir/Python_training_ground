import sqlite3
import json
from pathlib import Path

movies = json.loads(Path('movies.json').read_text())
print(movies)

# will create the file if it does not exist, these lines write data to the data base
# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'insert into movies values(?, ?, ?)'
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# reading data from a sqlite db
with sqlite3.connect('db.sqlite3') as conn:
    command = 'select * from movies'
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies2 = cursor.fetchall()
    print(movies2)
