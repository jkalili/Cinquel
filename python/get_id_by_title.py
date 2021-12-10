import sys
import time
from tmdb_dal import get_id_by_title
from errors import invalid_title_argument, invalid_title_syntax

start_time = time.time()
if len(sys.argv) != 2:
    raise Exception(invalid_title_argument)
    exit(1)


title = sys.argv[1]

result = get_id_by_title(title)
if not result:
    raise Exception(invalid_title_syntax)
print(f'\nThe query for "{title}" returned {len(result)} movies:\n')
print('ID     | Title \n')
for entry in result:
    print(f'{entry["m"]["movieId"]}  |  {entry["m"]["title"]}\n')
print(f'Elapsed time: {round(time.time() - start_time, 5)}')
