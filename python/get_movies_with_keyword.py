import sys
from tmdb_dal import get_movies_with_keyword
if len(sys.argv) != 2:
    print('Usage: get_movies_with_keyword <castId>')
    exit(1)


keyword = sys.argv[1]
invalid_id = (
    f'"{keyword}" is an invalid identifier or does not exist. Please try again.')

result = get_movies_with_keyword(keyword)
if not result:
    raise Exception(invalid_id)
print(f'\nThere are {len(result)} entries related to: "{keyword}":\n')
for entry in result:
    print(f'{entry["m.title"]}\n')
