import sys
from tmdb_dal import acted_together
from errors import invalid_actor, invalid_actor_arguments
if len(sys.argv) != 3:
    raise Exception(invalid_actor_arguments)
    exit(1)


castID1 = sys.argv[1]
castID2 = sys.argv[2]

result = acted_together(castID1, castID2)
if not result:
    raise Exception(invalid_actor)
print(
    f"Actors {castID1} and {castID2} have appeared together in {len(result)} movies\n")

for entry in result:
    print(f'{entry["m"]["title"]}\n')
