import sys
from tmdb_dal import link_actor_with_movies
from errors import invalid_actor_link_syntax, invalid_actor_link_argument

try:
    actor = str(input("Please input the actor to link: <actor name>"))
    relationships = list(tuple(map(str, input('Relationship: <movieId, role>: ').split(', '))) for r in range(
        int(input('Please enter number of relationships to add: '))))
except ValueError:
    raise Exception()  # TODO


result = link_actor_with_movies(actor, relationships)
if not result:
    raise Exception(invalid_actor_link_argument)
print(
    f'\n Added {len(result)} relationships for {actor} with role attributes:\n')
for entry in result:
    print(entry)
