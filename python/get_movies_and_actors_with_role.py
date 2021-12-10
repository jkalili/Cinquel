import sys
from tmdb_dal import get_movies_and_actors_with_role
from errors import invalid_actor_role_syntax, invalid_actor_role_argument
if len(sys.argv) != 2:
    raise Exception(invalid_actor_role_syntax)
    exit(1)


role = sys.argv[1]
result = get_movies_and_actors_with_role(role)
if not result:
    raise Exception(invalid_actor_role_argument)
print(
    f'\n The character "{role}" has appeared in the following {len(result)} movies:\n')
for entry in result:
    print(
        f'movie: {entry["r"][2]["title"]} | portrayed by: {entry["c"]["castID"]}\n')
