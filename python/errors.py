# Add Movie Errors
invalid_add_syntax = (
    'Please regard the following format: <budget: int> <movieId: str> <original_language: str> <popularity: float> <release_date: Date> <runtime: int> <title: str> <vote_average: float>')

invalid_add_argument = (
    'Usage: insert_movie <budget> <movieId> <original_language> <popularity> <release_date> <runtime> <title> <vote_average>')

invalid_add_id = (
    'Sorry, the specified ID is already in use. Please try again.')

# Find by Title Errors
invalid_title_syntax = ('Usage: find_movie_by_title <title>')

invalid_title_argument = (
    'The specified title is invalid or does not exist. Please try again.')

# Get Actor Performances Errors
invalid_actor_syntax = ('Usage: get_actor_performances <castId>')

invalid_actor_argument = (
    'The specified actor is an invalid identifier or does not exist. Please try again.')

# Remove Movie Errors
invalid_movie_syntax = ('Usage: remove_movie <movieID>')

invalid_movie_id = ('The specified ID is invalid.')


# Get Average Rating Errors
invalid_rating_syntax = ('Usage: get_average_rating <movieId>')

invalid_rating_argument = (
    'The specified argument does not match the required format. Please try again.')

invalid_rating_id = ('The specified movieID did not exist. Please try again.')


# Title Errors
invalid_movieID_syntax = ('Usage: get_title_by_id <movieID>')

invalid_movieID_argument = (
    'The specified movieID did not match the required format or does not exist. Please try again')


# Get Movies with Keyword Errors
invalid_keyword_syntax = ('Usage: get_movies_with_keyword <keyword>')

invalid_keyword_argument = (
    'The specified keyword is an invalid identifier or there are no movies that match that keyword. Please try again')


# Get Id by Title Errors
invalid_title_syntax = ('Usage: get_id_by_title <title>')

# Update Movie Budget Errors
invalid_movie_budget_syntax = (
    'Usage: update_movie_runtime <movieId> <updated_budget>')

invalid_movie_budget_argument = (
    "The specified movie budget does not match the required format. Please try again")

# Update Movie Original Language Errors
invalid_language_syntax = (
    'Usage: update_movie_original_language <movieId> <updated_original_language>')

invalid_language_argument = (
    'The specified language does not match the required format. Please try again')

# Update Movie Popularity Errors
invalid_popularity_syntax = (
    'Usage: update_movie_popularity <movieId> <updated_popularity>')

invalid_popularity_argument = (
    'The specified popularity does not match the required format. Please try again')

# Update Release Date Errors
invalid_date_syntax = (
    'Usage: update_movie_release_date <movieId> <updated_release_date>')

invalid_date_argument = (
    'The specified date does not match the required format. Please try again')

# Update Movie Runtime Errors
invalid_runtime_syntax = (
    'Usage: update_movie_runtime <movieId> <updated_runtime>')

invalid_runtime_argument = (
    'The specified runtime does not match the required format. Please try again')

# Update Movie Title Errors
invalid_update_title_syntax = (
    'Usage: update_movie_title <movieId> <updated_title>')

invalid_update_title_argument = (
    'The specified title does not match the required format. Please try again')

# Update Movie Vote Average Errors
invalid_update_vote_syntax = (
    'Usage: update_movie_vote_average <movieId> <updated_vote_average>')

invalid_update_vote_argument = (
    'The specified vote average does not match the required format. Please try again')

# Get Movies and Actors with Roles Errors
invalid_actor_role_syntax = ('Usage: get_movies_and_actors_with_role <role>')

invalid_actor_role_argument = (
    'The specified role does not match the required format or does not exist. Please try again')

# Get movies and Directors with Keyword Errors
invalid_movie_director_keyword_syntax = (
    'Usage: get_movies_and_directors_with_keyword <keyword>')

invalid_movie_director_keyword_argument = (
    'The specified keyword does not match the required format or does not exist. Please try again')
