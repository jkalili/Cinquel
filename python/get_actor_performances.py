import sys
from tmdb_dal import get_actor_performances
from errors import invalid_actor_syntax, invalid_actor_argument
if len(sys.argv) != 2:
    raise Exception(invalid_actor_argument)


try:
    castId = str(sys.argv[1])
except ValueError:
    raise Exception(invalid_actor_syntax)
print(castId)
result = get_actor_performances(castId)
if not result:
    raise Exception(invalid_actor_argument)
print(f'\n{castId} has performed in the following {len(result)} movies:\n')
for entry in result:
    print(f'movie: {entry["m.title"]} | role: {entry["r.role"]}\n')
