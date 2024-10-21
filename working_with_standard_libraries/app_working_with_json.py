import json
from pathlib import Path

# movies = [
#     {'id': 1, 'title': 'the greate gatsby', 'year': 2013},
#     {'id': 2, 'title': 'mulan', 'year': 1998}
# ]

#writing to a json file
# data = json.dumps(movies)
# Path('movies.json').write_text(data)

data = Path('movies.json').read_text()
movies = json.loads(data)
print(movies[0]['title'])