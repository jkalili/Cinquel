import sys
from tmdb_dal import link_actor_with_two_movies
from errors import invalid_actor_link_syntax, invalid_actor_link_argument, invalid_movie_id

try:
    actor = str(sys.argv[1])
    first_relationship = (str(sys.argv[2]), str(sys.argv[3]))
    second_relationship = (str(sys.argv[4]), str(sys.argv[5]))
    relationships = [first_relationship, second_relationship]
except (ValueError, IndexError):
    raise Exception(invalid_actor_link_syntax)


result = link_actor_with_two_movies(actor, relationships)
if not result:
    raise Exception(invalid_movie_id)
print(
    f'\n Added 2 relationships for {actor} with role attributes:\n')
print(
    f"{actor} as {relationships[0][1]} in {relationships[0][0]}")
print(
    f"{actor} as {relationships[1][1]} in {relationships[1][0]}")
