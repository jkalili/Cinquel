import sys
from tmdb_dal import get_actor_performances
if len(sys.argv) != 2:
    print('Usage: get_actor_performances <castId>')
    exit(1)


castId = sys.argv[1]
invalid_id = (
    f'"{castId}" is an invalid identifier or does not exist. Please try again. Note this could be a casing error')

result = get_actor_performances(castId)
if not result:
    raise Exception(invalid_id)
print(f'\n{castId} has performed in the following {len(result)} movies:\n')
for entry in result:
    print(f'movie: {entry["m.title"]} | role: {entry["r.role"]}\n')
