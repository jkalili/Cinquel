import sys
from tmdb_dal import acted_together
from errors import invalid_actor_syntax, invalid_actor_argument
if len(sys.argv) != 3:
    raise Exception(invalid_actor_argument)
    exit(1)


first_cast_id = sys.argv[1]
second_cast_id = sys.argv[2]

result = acted_together(first_cast_id, second_cast_id)
if not result:
    raise Exception(invalid_actor_syntax)
print(
    f"Actors {first_cast_id} and {second_cast_id} have appeared together in {len(result)} movies:\n")

for entry in result:
    print(f'{entry["m"]["title"]}\n')
