import sys
from tmdb_dal import get_movies_with_keyword
from errors import invalid_keyword_syntax, invalid_keyword_argument
if len(sys.argv) != 2:
    raise Exception(invalid_keyword_syntax)
    exit(1)


keyword = sys.argv[1]

result = get_movies_with_keyword(keyword)
if not result:
    raise Exception(invalid_keyword_argument)
print(f'\nThere are {len(result)} entries related to: "{keyword}":\n')
for entry in result:
    print(f'{entry["m.title"]}\n')
